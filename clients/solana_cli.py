#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.mnemonics.bip39 import (
    BIP39Mnemonic, BIP39_MNEMONIC_LANGUAGES, BIP39_MNEMONIC_WORDS
)
from hdwallet.seeds.bip39 import BIP39Seed
from hdwallet.cryptocurrencies import Solana as Cryptocurrency
from hdwallet.hds import BIP44HD

import json

# Get BIP39 mnemonic
mnemonic: str = BIP39Mnemonic.from_words(
    words=BIP39_MNEMONIC_WORDS.FIFTEEN, language=BIP39_MNEMONIC_LANGUAGES.CHINESE_TRADITIONAL
)
bip39_mnemonic: BIP39Mnemonic = BIP39Mnemonic(mnemonic=mnemonic)
print("BIP39 Mnemonic:", bip39_mnemonic.mnemonic())
print("BIP39 Language:", bip39_mnemonic.language())
print("BIP39 Words:", bip39_mnemonic.words())

# Get BIP39 seed
seed: str = BIP39Seed.from_mnemonic(
    mnemonic=bip39_mnemonic, passphrase=None
)

# Initialize Solana HDWallet
hdwallet: HDWallet = HDWallet(
    cryptocurrency=Cryptocurrency,
    hd=BIP44HD,
    network=Cryptocurrency.NETWORKS.MAINNET,
    passphrase=None
).from_private_key(   # Get Solana HDWallet from private key
    private_key=seed[:64]  # Use the first 64-length seed directly as private key
)

print(json.dumps(hdwallet.dump(exclude={
    "root", "indexes", "xprivate_key", "xpublic_key"
}), indent=4, ensure_ascii=False))

