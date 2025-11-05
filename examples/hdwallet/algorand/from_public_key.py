#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.cryptocurrencies import Algorand as Cryptocurrency
from hdwallet.hds import AlgorandHD

import json


hdwallet: HDWallet = HDWallet(
    cryptocurrency=Cryptocurrency,
    hd=AlgorandHD
).from_public_key(
    public_key="00c76d02311731bdca7afe7907f2f3b53383d43f278d8c22abb73c17d417d37cf1"
)

print(json.dumps(hdwallet.dump(exclude={"indexes"}), indent=4, ensure_ascii=False))

# print("Cryptocurrency:", hdwallet.cryptocurrency())
# print("Symbol:", hdwallet.symbol())
# print("Network:", hdwallet.network())
# print("Coin Type:", hdwallet.coin_type())
# print("ECC:", hdwallet.ecc())
# print("HD:", hdwallet.hd())
# print("Semantic:", hdwallet.semantic())
# print("Public Key:", hdwallet.public_key())
# print("Hash:", hdwallet.hash())
# print("Fingerprint:", hdwallet.fingerprint())
# print("Address:", hdwallet.address())
