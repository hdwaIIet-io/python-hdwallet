#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.cryptocurrencies import Algorand as Cryptocurrency
from hdwallet.derivations import CustomDerivation
from hdwallet.hds import AlgorandHD

import json


hdwallet: HDWallet = HDWallet(
    cryptocurrency=Cryptocurrency,
    hd=AlgorandHD
).from_xpublic_key(
    xpublic_key="xpub661MyMwAqRbcEiUJew81QNEAr6jYLVSksDzdQUtWbSWLRdA8ouX1bqK1WxS4qdF4gu8VwSxDVX7n216daK1735md81Z1L7uFUAAT4eSN1xr",
    strict=True
).from_derivation(
    derivation=CustomDerivation(
        path="m/0/0-2"  # Hardened "'" key is not allowed for xpublic key
    )
)

# print(json.dumps(hdwallet.dump(exclude={"indexes"}), indent=4, ensure_ascii=False))
print(json.dumps(hdwallet.dumps(exclude={"indexes"}), indent=4, ensure_ascii=False))

# print("Cryptocurrency:", hdwallet.cryptocurrency())
# print("Symbol:", hdwallet.symbol())
# print("Network:", hdwallet.network())
# print("Coin Type:", hdwallet.coin_type())
# print("ECC:", hdwallet.ecc())
# print("HD:", hdwallet.hd())
# print("Semantic:", hdwallet.semantic())
# print("Root XPublic Key:", hdwallet.root_xpublic_key())
# print("Root Chain Code:", hdwallet.root_chain_code())
# print("Root Public Key:", hdwallet.root_public_key())
# print("Strict:", hdwallet.strict())
# print("Path:", hdwallet.path())
# print("Depth:", hdwallet.depth())
# print("Indexes:", hdwallet.indexes())
# print("Index:", hdwallet.index())
# print("XPublic Key:", hdwallet.xpublic_key())
# print("Chain Code:", hdwallet.chain_code())
# print("Public Key:", hdwallet.public_key())
# print("Hash:", hdwallet.hash())
# print("Fingerprint:", hdwallet.fingerprint())
# print("Parent Fingerprint:", hdwallet.parent_fingerprint())
# print("Address:", hdwallet.address())
