#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.cryptocurrencies import Bitcoin as Cryptocurrency
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
    semantic=SEMANTICS.P2WPKH_IN_P2SH
).from_xprivate_key(
    xprivate_key="xprv9s21ZrQH143K24t96gCaezzt1QQmnqiEGm8m6TP8yb8e3TmGfkCgcLEVsskufMW9R4KH27pD1kyyEfJkYz1eiPwjhFzB4gtabH3PzMSmXSM",
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
# print("Root WIF:", hdwallet.root_wif())
# print("Root Chain Code:", hdwallet.root_chain_code())
# print("Root Public Key:", hdwallet.root_public_key())
# print("Strict:", hdwallet.strict())
# print("Public Key Type:", hdwallet.public_key_type())
# print("WIF Type:", hdwallet.wif_type())
# print("Path:", hdwallet.path())
# print("Depth:", hdwallet.depth())
# print("Indexes:", hdwallet.indexes())
# print("Index:", hdwallet.index())
# print("XPrivate Key:", hdwallet.xprivate_key())
# print("XPublic Key:", hdwallet.xpublic_key())
# print("Private Key:", hdwallet.private_key())
# print("WIF:", hdwallet.wif())
# print("Chain Code:", hdwallet.chain_code())
# print("Public Key:", hdwallet.public_key())
# print("Uncompressed:", hdwallet.uncompressed())
# print("Compressed:", hdwallet.compressed())
# print("Hash:", hdwallet.hash())
# print("Fingerprint:", hdwallet.fingerprint())
# print("Parent Fingerprint:", hdwallet.parent_fingerprint())
# print("Address:", hdwallet.address())
