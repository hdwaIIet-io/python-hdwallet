#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.cryptocurrencies import Algorand as Cryptocurrency
from hdwallet.derivations import CustomDerivation
from hdwallet.hds import AlgorandHD

import json


hdwallet: HDWallet = HDWallet(
    cryptocurrency=Cryptocurrency,
    hd=AlgorandHD
).from_xprivate_key(
    xprivate_key="xprv3QESAWYc9vDdZKQAwwfoRBaiWEiTMbMtfPuyREap66sm2yyrV5ipveHVwDccQejWaLqMqLxDYnuNssg4Mf19Mc7EtNuGqLxZPdkaCnR9YEqo3qJpsqBnRi3qkWdWmFZ6xbhNUk799jZqiBwW3ou7jcS",
    strict=True
).from_derivation(
    derivation=CustomDerivation(
        path="m/0'/0-2"
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
# print("Root XPrivate Key:", hdwallet.root_xprivate_key())
# print("Root XPublic Key:", hdwallet.root_xpublic_key())
# print("Root Private Key:", hdwallet.root_private_key())
# print("Root Chain Code:", hdwallet.root_chain_code())
# print("Root Public Key:", hdwallet.root_public_key())
# print("Path Key:", hdwallet.path_key())
# print("Strict:", hdwallet.strict())
# print("Path:", hdwallet.path())
# print("Depth:", hdwallet.depth())
# print("Indexes:", hdwallet.indexes())
# print("Index:", hdwallet.index())
# print("XPrivate Key:", hdwallet.xprivate_key())
# print("XPublic Key:", hdwallet.xpublic_key())
# print("Private Key:", hdwallet.private_key())
# print("Chain Code:", hdwallet.chain_code())
# print("Public Key:", hdwallet.public_key())
# print("Hash:", hdwallet.hash())
# print("Fingerprint:", hdwallet.fingerprint())
# print("Parent Fingerprint:", hdwallet.parent_fingerprint())
# print("Address:", hdwallet.address())
