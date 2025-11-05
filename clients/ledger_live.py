#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.mnemonics import (
    BIP39Mnemonic, BIP39_MNEMONIC_LANGUAGES, BIP39_MNEMONIC_WORDS
)
from hdwallet.cryptocurrencies import Ethereum as Cryptocurrency
from hdwallet.hds import BIP44HD
from hdwallet.derivations import (
    BIP44Derivation, CHANGES
)

# Initialize Ethereum HDWallet
hdwallet: HDWallet = HDWallet(
    cryptocurrency=Cryptocurrency,
    hd=BIP44HD,
    network=Cryptocurrency.NETWORKS.MAINNET,
    passphrase=None  # "hdwallet-io"
).from_mnemonic(   # Get Ethereum HDWallet from mnemonic phrase
    mnemonic=BIP39Mnemonic(
        mnemonic=BIP39Mnemonic.from_words(
            words=BIP39_MNEMONIC_WORDS.TWENTY_FOUR,
            language=BIP39_MNEMONIC_LANGUAGES.ENGLISH
        )
    )
).from_derivation(  # Drive from BIP44 derivation
    derivation=BIP44Derivation(
        coin_type=Cryptocurrency.COIN_TYPE,
        account=(0, 10),  # or "0-10",
        change=CHANGES.EXTERNAL_CHAIN,
        address=0
    )
)

print("Mnemonic:", hdwallet.mnemonic())
print("Base HD Path:  m/44'/60'/{account}'/0/0", "\n")

# Print dived Ethereum HDWallet information's
for derivation in hdwallet.dumps(exclude={"root", "indexes"}):
    # Print path, address and private_key
    print(f"{derivation['at']['path']} {derivation['address']} 0x{derivation['private_key']}")
