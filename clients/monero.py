#!/usr/bin/env python3

from typing import (
    Optional, Union
)

from hdwallet.entropies.monero import (
    MoneroEntropy, MONERO_ENTROPY_STRENGTHS
)
from hdwallet.mnemonics.monero import (
    MoneroMnemonic, MONERO_MNEMONIC_LANGUAGES
)
from hdwallet.cryptocurrencies import Monero
from hdwallet.seeds.monero import MoneroSeed
from hdwallet.hds.monero import MoneroHD


# Generate Monero entropy
entropy: str = MoneroEntropy.generate(
    strength=MONERO_ENTROPY_STRENGTHS.TWO_HUNDRED_FIFTY_SIX
)
monero_entropy: MoneroEntropy = MoneroEntropy(entropy=entropy)
print("Monero Entropy:", monero_entropy.entropy())
print("Monero Strength:", monero_entropy.strength())

# Get Monero mnemonic
mnemonic: str = MoneroMnemonic.from_entropy(
    entropy=monero_entropy, language=MONERO_MNEMONIC_LANGUAGES.ENGLISH, checksum=True
)
monero_mnemonic: MoneroMnemonic = MoneroMnemonic(mnemonic=mnemonic)
print("Monero Mnemonic:", monero_mnemonic.mnemonic())
print("Monero Language:", monero_mnemonic.language())
print("Monero Words:", monero_mnemonic.words())

# Get Monero seed
seed: str = MoneroSeed.from_mnemonic(
    mnemonic=monero_mnemonic
)
monero_seed: MoneroSeed = MoneroSeed(seed=seed)

# Initialize Monero HD
monero_hd: MoneroHD = MoneroHD(
    network=Monero.NETWORKS.MAINNET
)

# Update Monero HD root keys from seed
monero_hd.from_seed(
    seed=monero_seed
)

# Dump all keys
print("Monero Spend Private Key:", monero_hd.spend_private_key())
print("Monero View Private Key:", monero_hd.view_private_key())
print("Monero Spend Public Key:", monero_hd.spend_public_key())
print("Monero View Public Key:", monero_hd.view_public_key())
print("Monero Primary Address:", monero_hd.primary_address())

# With payment ID
PAYMENT_ID: Optional[Union[bytes, str]] = "ad17dc6e6793d178"
print("Monero Payment ID:", PAYMENT_ID)
print("Monero Integrated Address:", monero_hd.integrated_address(payment_id=PAYMENT_ID))

# Miner indexes length
MINER_INDEXES: int = 2
# Major indexes length
MAJOR_INDEXES: int = 5

for minor_index in range(MINER_INDEXES):
    for major_index in range(MAJOR_INDEXES):
        print(f"Monero Sub-Address (Minor: {minor_index}, Major: {major_index}):", monero_hd.sub_address(
            minor=minor_index, major=major_index
        ))
