#!/usr/bin/env python3

from hdwallet.hds import CardanoHD
from hdwallet.derivations import CustomDerivation
from hdwallet.cryptocurrencies import Cardano

cardano_hd: CardanoHD = CardanoHD(
    cardano_type=Cardano.TYPES.BYRON_LEGACY
)

seed = "aa88d53b805f411823f57c797c88bfab1454f5eee5f7b2bafeabeadac2cc59fe"
xprivate_key = "xprv3QESAWYc9vDdZTncakVdLLPy3cLJYsPCkkFseh6jb96oDBK4x4ZGBpjvRtTSmgeho8L2CDXEBsGdziVKgdFs9Fs34AcnR9d2jGVQa2DDSfsTbTunTdQTjFZMpoDFt4xb2Eg4xoU4cRA5KNUmCSnuGJG"
xpublic_key = "xpub661MyMwAqRbcFChpDRzR18jyqTYumPn32qGVKzFqCqy6t6Dz3otrQArHo1YDXHNd39vycLYs97sDJtENPcj7VSgZZWHiK8H2udWSzhR3QY5"

cardano_hd.from_seed(seed=seed)
# cardano_hd.from_xprivate_key(xprivate_key=xprivate_key)
# cardano_hd.from_xpublic_key(xpublic_key=xpublic_key)

custom_derivation: CustomDerivation = CustomDerivation(
    path="m/0'/0"
)
cardano_hd.from_derivation(derivation=custom_derivation)

print("Seed:", cardano_hd.seed())
print("Root XPrivate Key:", cardano_hd.root_xprivate_key())
print("Root XPublic Key:", cardano_hd.root_xpublic_key())
print("Root Private Key:", cardano_hd.root_private_key())
print("Root Chain Code:", cardano_hd.root_chain_code())
print("Root Public Key:", cardano_hd.root_public_key())

print("XPrivate Key:", cardano_hd.xprivate_key())
print("XPublic Key:", cardano_hd.xpublic_key())
print("Private Key:", cardano_hd.private_key())
print("Chain Code:", cardano_hd.chain_code())
print("Public Key:", cardano_hd.public_key())
print("Public Key Type:", cardano_hd.public_key_type())
print("Compressed:", cardano_hd.compressed())
print("Uncompressed:", cardano_hd.uncompressed())
print("Hash:", cardano_hd.hash())
print("Fingerprint:", cardano_hd.fingerprint())
print("Parent Fingerprint:", cardano_hd.parent_fingerprint())
print("Depth:", cardano_hd.depth())
print("Path:", cardano_hd.path())
print("Path Key:", cardano_hd.path_key())
print("Index:", cardano_hd.index())
print("Indexes:", cardano_hd.indexes())
print("getStrict:", cardano_hd.strict())
print("Address:", cardano_hd.address())
