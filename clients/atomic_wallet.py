#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.mnemonics import BIP39Mnemonic
from hdwallet.cryptocurrencies import Ethereum as Cryptocurrency
from hdwallet.hds import BIP32HD

import json

# Initialize Ethereum HDWallet
hdwallet: HDWallet = HDWallet(
    cryptocurrency=Cryptocurrency,
    hd=BIP32HD,
    network=Cryptocurrency.NETWORKS.MAINNET,
    passphrase=None
).from_mnemonic(   # Get Ethereum HDWallet from mnemonic phrase
    mnemonic=BIP39Mnemonic(
        mnemonic="abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"
    )
)

# Print root keys
print(json.dumps(hdwallet.dump(exclude={"indexes"}), indent=4, ensure_ascii=False))
