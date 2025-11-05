#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.mnemonics import BIP39Mnemonic
from hdwallet.seeds import BIP39Seed
from hdwallet.cryptocurrencies import Ethereum as Cryptocurrency
from hdwallet.hds import BIP44HD
from hdwallet.derivations import (
    BIP44Derivation, CHANGES
)

import json

# 24-words mnemonic phrase
MNEMONIC: str = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon " \
                "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon art"

# Initialize Ethereum HDWallet
hdwallet: HDWallet = HDWallet(
    cryptocurrency=Cryptocurrency,
    hd=BIP44HD,
    network=Cryptocurrency.NETWORKS.MAINNET,
    passphrase=None
).from_seed(   # Get Ethereum HDWallet from seed
    seed=BIP39Seed(
        seed=BIP39Mnemonic.decode(mnemonic=MNEMONIC)  # Use decoded mnemonic (entropy) directly as seed
    )
).from_derivation(  # Drive from BIP44 derivation
    derivation=BIP44Derivation(
        coin_type=Cryptocurrency.COIN_TYPE,
        account=0,
        change=CHANGES.EXTERNAL_CHAIN,
        address=0
    )
)

# Same address of Brave crypto wallets extension
# print(json.dumps(hdwallet.dump(exclude={"indexes"}), indent=4, ensure_ascii=False))
print(f"Address: {hdwallet.address()}")
