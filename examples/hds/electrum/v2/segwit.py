#!/usr/bin/env python3

from hdwallet.hds import ElectrumV2HD
from hdwallet.cryptocurrencies import Bitcoin as Cryptocurrency
from hdwallet.consts import MODES, PUBLIC_KEY_TYPES
from hdwallet.derivations import ElectrumDerivation

electrum_v2_hd: ElectrumV2HD = ElectrumV2HD(
    mode=MODES.SEGWIT,
    public_key_type=PUBLIC_KEY_TYPES.UNCOMPRESSED,
    wif_prefix=Cryptocurrency.NETWORKS.MAINNET.WIF_PREFIX
)

seed = "cf9d920a1e95f1304ff77d50a15bc06e17eead71947d766780ce9a9ad4efb286e64481542f080c5901a4b3487793a252c5354ab7e6576301a5a08c5b9d771f8a"

electrum_v2_hd.from_seed(seed=seed)

print("Mode:", electrum_v2_hd.mode())
print("Seed:", electrum_v2_hd.seed())
print("Master Private Key:", electrum_v2_hd.master_private_key())
print("Master WIF:", electrum_v2_hd.master_wif())
print("Master Public Key:", electrum_v2_hd.master_public_key())
print("Public Key Type:", electrum_v2_hd.public_key_type())
print("WIF Type:", electrum_v2_hd.wif_type())

electrum_derivation: ElectrumDerivation = ElectrumDerivation(
    change=0, address=0
)

electrum_v2_hd.from_derivation(derivation=electrum_derivation)

print("Private Key:", electrum_v2_hd.private_key())
print("WIF:", electrum_v2_hd.wif())
print("Public Key:", electrum_v2_hd.public_key())
print("Uncompressed:", electrum_v2_hd.uncompressed())
print("Compressed:", electrum_v2_hd.compressed())
print("Address:", electrum_v2_hd.address())
