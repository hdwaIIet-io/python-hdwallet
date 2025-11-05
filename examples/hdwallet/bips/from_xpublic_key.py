#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.cryptocurrencies import Qtum as Cryptocurrency
from hdwallet.derivations import CustomDerivation
from hdwallet.consts import (
    PUBLIC_KEY_TYPES, SEMANTICS
)
from hdwallet.hds import BIP141HD

import json


hdwallet: HDWallet = HDWallet(
    cryptocurrency=Cryptocurrency,
    hd=BIP141HD,
    network=Cryptocurrency.NETWORKS.MAINNET,
    public_key_type=PUBLIC_KEY_TYPES.COMPRESSED,
    semantic=SEMANTICS.P2WSH
).from_xpublic_key(
    xpublic_key="xpub661MyMwAqRbcEYxcChjb28wcZSFGCJS5dz4MtqnkXvfcvG6RDHWwA8Yyj8huR1AnPaWwMjjwux3n6b5hNnTcgwYXSfCsi9RnQ6RvY3RZ8fm",
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
# print("Public Key Type:", hdwallet.public_key_type())
# print("Path:", hdwallet.path())
# print("Depth:", hdwallet.depth())
# print("Indexes:", hdwallet.indexes())
# print("Index:", hdwallet.index())
# print("XPublic Key:", hdwallet.xpublic_key())
# print("Chain Code:", hdwallet.chain_code())
# print("Public Key:", hdwallet.public_key())
# print("Uncompressed:", hdwallet.uncompressed())
# print("Compressed:", hdwallet.compressed())
# print("Hash:", hdwallet.hash())
# print("Fingerprint:", hdwallet.fingerprint())
# print("Parent Fingerprint:", hdwallet.parent_fingerprint())
# print("Address:", hdwallet.address())
