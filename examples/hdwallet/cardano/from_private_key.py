#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.cryptocurrencies import Cardano as Cryptocurrency
from hdwallet.hds import CardanoHD

import json


hdwallet: HDWallet = HDWallet(
    cryptocurrency=Cryptocurrency,
    hd=CardanoHD,
    cardano_type=Cryptocurrency.TYPES.SHELLEY_ICARUS,
    address_type=Cryptocurrency.ADDRESS_TYPES.STAKING
).from_private_key(
    private_key="a00f697f4eeafd98efb151ea16bd84451a3071eae3427a47d67a3361608b0656724e9a307aab119a07d3175f2a8f61dfcdcfc7f0e2e3138282dca388ea58f3ff"
)

print(json.dumps(hdwallet.dump(exclude={"indexes"}), indent=4, ensure_ascii=False))

# print("Cryptocurrency:", hdwallet.cryptocurrency())
# print("Symbol:", hdwallet.symbol())
# print("Network:", hdwallet.network())
# print("Coin Type:", hdwallet.coin_type())
# print("ECC:", hdwallet.ecc())
# print("HD:", hdwallet.hd())
# print("Cardano Type:", hdwallet.cardano_type())
# print("Semantic:", hdwallet.semantic())
# print("Private Key:", hdwallet.private_key())
# print("Public Key:", hdwallet.public_key())
# print("Hash:", hdwallet.hash())
# print("Fingerprint:", hdwallet.fingerprint())
# print("Address:", hdwallet.address())
