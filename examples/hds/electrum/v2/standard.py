#!/usr/bin/env python3

from hdwallet.hds import ElectrumV2HD
from hdwallet.cryptocurrencies import Bitcoin as Cryptocurrency
from hdwallet.consts import MODES, PUBLIC_KEY_TYPES
from hdwallet.derivations import ElectrumDerivation

electrum_v2_hd: ElectrumV2HD = ElectrumV2HD(
    mode=MODES.STANDARD,
    public_key_type=PUBLIC_KEY_TYPES.UNCOMPRESSED,
    wif_prefix=Cryptocurrency.NETWORKS.MAINNET.WIF_PREFIX
)

seed = "22e0c334cf22eb3c8a93ade2e0d1c43aa979a4426212e6c4099ff4d49434a0c6eecfd1437a79e11ad08605acc94f0255bd77a0728ed9693ab549c385fe610300"

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
