#!/usr/bin/env python3

from hdwallet.entropies import (
    MoneroEntropy, MONERO_ENTROPY_STRENGTHS
)
from hdwallet.mnemonics import MONERO_MNEMONIC_LANGUAGES
from hdwallet.cryptocurrencies import Monero as Cryptocurrency
from hdwallet.derivations import MoneroDerivation
from hdwallet.hds import MoneroHD
from hdwallet import HDWallet

import json


hdwallet: HDWallet = HDWallet(
    cryptocurrency=Cryptocurrency,
    hd=MoneroHD,
    network=Cryptocurrency.NETWORKS.MAINNET,
    language=MONERO_MNEMONIC_LANGUAGES.PORTUGUESE,
    payment_id="ad17dc6e6793d178"
).from_entropy(
    entropy=MoneroEntropy(
        entropy=MoneroEntropy.generate(
            strength=MONERO_ENTROPY_STRENGTHS.ONE_HUNDRED_TWENTY_EIGHT
        )
    )
).from_derivation(
    derivation=MoneroDerivation(
        minor=0, major=5
    )
)

# print(json.dumps(hdwallet.dump(), indent=4, ensure_ascii=False))
print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))

# print("Cryptocurrency:", hdwallet.cryptocurrency())
# print("Symbol:", hdwallet.symbol())
# print("Network:", hdwallet.network())
# print("Coin Type:", hdwallet.coin_type())
# print("Entropy:", hdwallet.entropy())
# print("Strength:", hdwallet.strength())
# print("Mnemonic:", hdwallet.mnemonic())
# print("Language:", hdwallet.language())
# print("Seed:", hdwallet.seed())
# print("ECC:", hdwallet.ecc())
# print("HD:", hdwallet.hd())
# print("Spend Private Key:", hdwallet.spend_private_key())
# print("View Private Key:", hdwallet.view_private_key())
# print("Spend Public Key:", hdwallet.spend_public_key())
# print("View Public Key:", hdwallet.view_public_key())
# print("Primary Address:", hdwallet.primary_address())
# print("Integrated Address:", hdwallet.integrated_address())
# print("Sub Address:", hdwallet.sub_address())
