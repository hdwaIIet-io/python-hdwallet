#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.cryptocurrencies import Bitcoin as Cryptocurrency
from hdwallet.consts import PUBLIC_KEY_TYPES
from hdwallet.hds import BIP49HD

import json


hdwallet: HDWallet = HDWallet(
    cryptocurrency=Cryptocurrency,
    hd=BIP49HD,
    network=Cryptocurrency.NETWORKS.MAINNET,
    public_key_type=PUBLIC_KEY_TYPES.COMPRESSED
).from_private_key(
    private_key="0fea3ff3b19b033672e8ac8a3b26fed252daf30762c8294e9dd62dc417d2108e"
)

print(json.dumps(hdwallet.dump(exclude={"indexes"}), indent=4, ensure_ascii=False))

# print("Cryptocurrency:", hdwallet.cryptocurrency())
# print("Symbol:", hdwallet.symbol())
# print("Network:", hdwallet.network())
# print("Coin Type:", hdwallet.coin_type())
# print("ECC:", hdwallet.ecc())
# print("HD:", hdwallet.hd())
# print("Semantic:", hdwallet.semantic())
# print("Public Key Type:", hdwallet.public_key_type())
# print("WIF Type:", hdwallet.wif_type())
# print("Private Key:", hdwallet.private_key())
# print("WIF:", hdwallet.wif())
# print("Public Key:", hdwallet.public_key())
# print("Uncompressed:", hdwallet.uncompressed())
# print("Compressed:", hdwallet.compressed())
# print("Hash:", hdwallet.hash())
# print("Fingerprint:", hdwallet.fingerprint())
# print("Address:", hdwallet.address())
