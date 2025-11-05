#!/usr/bin/env python3

from hdwallet.hds import ElectrumV1HD
from hdwallet.cryptocurrencies import Bitcoin as Cryptocurrency
from hdwallet.derivations import ElectrumDerivation
from hdwallet.consts import PUBLIC_KEY_TYPES

electrum_v1_hd: ElectrumV1HD = ElectrumV1HD(
    public_key_type=PUBLIC_KEY_TYPES.COMPRESSED,
    wif_prefix=Cryptocurrency.NETWORKS.MAINNET.WIF_PREFIX
)

seed = "7c2548ab89ffea8a6579931611969ffc0ed580ccf6048d4230762b981195abe5"
private_key = "7c2548ab89ffea8a6579931611969ffc0ed580ccf6048d4230762b981195abe5"
wif = "L1P2uu8DXVF8AQaR3hLoxsr8XvdMyWuhs9F8HjLYAPirhQTc8jgy"
public_key = "034e13b0f311a55b8a5db9a32e959da9f011b131019d4cebe6141b9e2c93edcbfc"

# electrum_v1_hd.from_seed(seed=seed)
electrum_v1_hd.from_private_key(private_key=private_key)
# electrum_v1_hd.from_wif(wif=wif)
# electrum_v1_hd.from_public_key(public_key=public_key)

print("Seed:", electrum_v1_hd.seed())
print("Master Private Key:", electrum_v1_hd.master_private_key())
print("Master WIF:", electrum_v1_hd.master_wif())
print("Master Public Key:", electrum_v1_hd.master_public_key())
print("Public Key Type:", electrum_v1_hd.public_key_type())
print("WIF Type:", electrum_v1_hd.wif_type())

electrum_derivation: ElectrumDerivation = ElectrumDerivation(
    change=0, address=15
)

electrum_v1_hd.from_derivation(derivation=electrum_derivation)

print("Private Key:", electrum_v1_hd.private_key())
print("WIF:", electrum_v1_hd.wif())
print("Public Key:", electrum_v1_hd.public_key())
print("Uncompressed:", electrum_v1_hd.uncompressed())
print("Compressed:", electrum_v1_hd.compressed())
print("Address:", electrum_v1_hd.address())
