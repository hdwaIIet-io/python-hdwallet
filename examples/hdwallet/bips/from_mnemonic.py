#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.mnemonics import (
    BIP39Mnemonic, BIP39_MNEMONIC_LANGUAGES, MONERO_MNEMONIC_WORDS
)
from hdwallet.cryptocurrencies import Binance as Cryptocurrency
from hdwallet.consts import PUBLIC_KEY_TYPES
from hdwallet.derivations import (
    BIP44Derivation, CHANGES
)
from hdwallet.hds import BIP32HD

import json


hdwallet: HDWallet = HDWallet(
    cryptocurrency=Cryptocurrency,
    hd=BIP32HD,
    network=Cryptocurrency.NETWORKS.MAINNET,
    public_key_type=PUBLIC_KEY_TYPES.COMPRESSED,
    passphrase="meherett"
).from_mnemonic(
    mnemonic=BIP39Mnemonic(
        mnemonic=BIP39Mnemonic.from_words(
            words=MONERO_MNEMONIC_WORDS.TWELVE,
            language=BIP39_MNEMONIC_LANGUAGES.ITALIAN
        )
    )
).from_derivation(
    derivation=BIP44Derivation(
        coin_type=Cryptocurrency.COIN_TYPE,
        account=0,
        change=CHANGES.EXTERNAL_CHAIN,
        address=0
    )
)

print(json.dumps(hdwallet.dump(exclude={"indexes"}), indent=4, ensure_ascii=False))
# print(json.dumps(hdwallet.dumps(exclude={"indexes"}), indent=4, ensure_ascii=False))

# print("Cryptocurrency:", hdwallet.cryptocurrency())
# print("Symbol:", hdwallet.symbol())
# print("Network:", hdwallet.network())
# print("Coin Type:", hdwallet.coin_type())
# print("Entropy:", hdwallet.entropy())
# print("Strength:", hdwallet.strength())
# print("Mnemonic:", hdwallet.mnemonic())
# print("Passphrase:", hdwallet.passphrase())
# print("Language:", hdwallet.language())
# print("Seed:", hdwallet.seed())
# print("ECC:", hdwallet.ecc())
# print("HD:", hdwallet.hd())
# print("Semantic:", hdwallet.semantic())
# print("Root XPrivate Key:", hdwallet.root_xprivate_key())
# print("Root XPublic Key:", hdwallet.root_xpublic_key())
# print("Root Private Key:", hdwallet.root_private_key())
# print("Root WIF:", hdwallet.root_wif())
# print("Root Chain Code:", hdwallet.root_chain_code())
# print("Root Public Key:", hdwallet.root_public_key())
# print("Strict:", hdwallet.strict())
# print("Public Key Type:", hdwallet.public_key_type())
# print("WIF Type:", hdwallet.wif_type())
# print("Path:", hdwallet.path())
# print("Depth:", hdwallet.depth())
# print("Indexes:", hdwallet.indexes())
# print("Index:", hdwallet.index())
# print("XPrivate Key:", hdwallet.xprivate_key())
# print("XPublic Key:", hdwallet.xpublic_key())
# print("Private Key:", hdwallet.private_key())
# print("WIF:", hdwallet.wif())
# print("Chain Code:", hdwallet.chain_code())
# print("Public Key:", hdwallet.public_key())
# print("Uncompressed:", hdwallet.uncompressed())
# print("Compressed:", hdwallet.compressed())
# print("Hash:", hdwallet.hash())
# print("Fingerprint:", hdwallet.fingerprint())
# print("Parent Fingerprint:", hdwallet.parent_fingerprint())
# print("Address:", hdwallet.address())
