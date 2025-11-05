#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.derivations import ElectrumDerivation
from hdwallet.cryptocurrencies import Bitcoin
from hdwallet.consts import PUBLIC_KEY_TYPES
from hdwallet.hds import ElectrumV1HD

import json


hdwallet: HDWallet = HDWallet(
    cryptocurrency=Bitcoin,
    hd=ElectrumV1HD,
    network=Bitcoin.NETWORKS.MAINNET,
    public_key_type=PUBLIC_KEY_TYPES.UNCOMPRESSED
).from_public_key(
    public_key="04da211622e04fc90a4264eac2f4294f74b0cbb23e4ed4c35796a8b188f9d66700c101441f9ed9a13e173f257d12e25a3870d7e2916e25c232d4c732af64e750b6"
).from_derivation(
    derivation=ElectrumDerivation(
        change=0, address=(1, 2)
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
# print("Master Public Key:", hdwallet.master_public_key())
# print("Public Key Type:", hdwallet.public_key_type())
# print("Public Key:", hdwallet.public_key())
# print("Uncompressed:", hdwallet.uncompressed())
# print("Compressed:", hdwallet.compressed())
# print("Address:", hdwallet.address())
