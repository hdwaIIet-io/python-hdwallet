#!/usr/bin/env python3

from typing import Type

import json

from hdwallet.mnemonics import BIP39Mnemonic
from hdwallet.cryptocurrencies import (
    ICryptocurrency, Bitcoin, Ethereum, Solana
)
from hdwallet.hds import (
    IHD, BIP32HD, BIP44HD, BIP49HD, BIP84HD
)
from hdwallet.derivations import (
    IDerivation, CustomDerivation, BIP44Derivation, BIP49Derivation, BIP84Derivation
)
from hdwallet.consts import PUBLIC_KEY_TYPES
from hdwallet.libs.base58 import encode
from hdwallet.utils import get_bytes
from hdwallet import HDWallet


mnemonic: BIP39Mnemonic = BIP39Mnemonic(
    mnemonic="abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"
)

standards: dict = {
    "solana": {
        "hd": BIP32HD,
        "derivation": CustomDerivation(path=Solana.DEFAULT_PATH)
    },
    "ethereum": {
        "hd": BIP44HD,
        "derivation": BIP44Derivation(coin_type=Ethereum.COIN_TYPE)
    },
    "bitcoin": {
        "legacy": {
            "hd": BIP44HD,
            "derivation": BIP44Derivation(coin_type=Bitcoin.COIN_TYPE)
        },
        "nested-segwit": {
            "hd": BIP49HD,
            "derivation": BIP49Derivation(coin_type=Bitcoin.COIN_TYPE)
        },
        "native-segwit": {
            "hd": BIP84HD,
            "derivation": BIP84Derivation(coin_type=Bitcoin.COIN_TYPE)
        }
    }
}

def generate_phantom_hdwallet(cryptocurrency: Type[ICryptocurrency], hd: Type[IHD], network: str, derivation: IDerivation, **kwargs) -> HDWallet:
    return HDWallet(cryptocurrency=cryptocurrency, hd=hd, network=network, kwargs=kwargs).from_mnemonic(mnemonic=mnemonic).from_derivation(derivation=derivation)

print("Mnemonic:", mnemonic.mnemonic(), "\n")

# Solana
solana_hdwallet: HDWallet = generate_phantom_hdwallet(
    cryptocurrency=Solana,
    hd=standards["solana"]["hd"],
    network=Solana.NETWORKS.MAINNET,
    derivation=standards["solana"]["derivation"]
)
print(f"{solana_hdwallet.cryptocurrency()} ({solana_hdwallet.symbol()}) wallet:", json.dumps(dict(
    path=solana_hdwallet.path(),
    base58=encode(get_bytes(
        solana_hdwallet.private_key() + solana_hdwallet.public_key()[2:]
    )),
    private_key=solana_hdwallet.private_key(),
    public_key=solana_hdwallet.public_key()[2:],
    address=solana_hdwallet.address()
), indent=4))

# Ethereum
ethereum_hdwallet: HDWallet = generate_phantom_hdwallet(
    cryptocurrency=Ethereum,
    hd=standards["ethereum"]["hd"],
    network=Ethereum.NETWORKS.MAINNET,
    derivation=standards["ethereum"]["derivation"]
)
print(f"{ethereum_hdwallet.cryptocurrency()} ({ethereum_hdwallet.symbol()}) wallet:", json.dumps(dict(
    path=ethereum_hdwallet.path(),
    private_key=f"0x{ethereum_hdwallet.private_key()}",
    public_key=ethereum_hdwallet.public_key(),
    address=ethereum_hdwallet.address()
), indent=4))

# Bitcoin (Legacy, Nested-SegWit, Native-SegWit)
for address_type in ["legacy", "nested-segwit", "native-segwit"]:

    bitcoin_hdwallet: HDWallet = generate_phantom_hdwallet(
        cryptocurrency=Bitcoin,
        hd=standards["bitcoin"][address_type]["hd"],
        network=Bitcoin.NETWORKS.MAINNET,
        derivation=standards["bitcoin"][address_type]["derivation"],
        public_key_type=PUBLIC_KEY_TYPES.COMPRESSED
    )
    print(f"{bitcoin_hdwallet.cryptocurrency()} ({bitcoin_hdwallet.symbol()}) {address_type} wallet:", json.dumps(dict(
        path=bitcoin_hdwallet.path(),
        wif=bitcoin_hdwallet.wif(),
        private_key=bitcoin_hdwallet.private_key(),
        public_key=bitcoin_hdwallet.public_key(),
        address=bitcoin_hdwallet.address()
    ), indent=4))
