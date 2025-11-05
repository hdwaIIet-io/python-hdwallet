#!/usr/bin/env python3

from hdwallet.hds import CardanoHD
from hdwallet.derivations import BIP44Derivation, CHANGES
from hdwallet.cryptocurrencies import Cardano

cardano_hd: CardanoHD = CardanoHD(
    cardano_type=Cardano.TYPES.BYRON_LEDGER
)

seed = "2f370832206daef44362eeb0327f1c04c4e64ce4535754e2d94656f6698382a243393120e71bdf9d4ae4543723aabe8477b20e473c6517b7971cd15a1e760960"
xprivate_key = "xprv3QESAWYc9vDdZnQAzoRU9TqGMCHQsNv54B6ZbYH9XBUxjS8dzG54TAvYnv3LGrxv8JJTA5CwppfcrELdK554QjuKHU678otKHdEUxniPYvXXnv5eaDKmGwEXQq3TwbFfbFJ3Ws5odsquz1PvnDbJ2z6"
xpublic_key = "xpub661MyMwAqRbcGHMw89APz6eSmz7oeCnWTLFtYuoUVaCwvTFHjVYeC79w5fwXsyNcN1GgvnZ6378pUqE2FkteESXiY4LutWk6Xni7fveKg7h"

cardano_hd.from_seed(seed=seed)
# cardano_hd.from_xprivate_key(xprivate_key=xprivate_key)
# cardano_hd.from_xpublic_key(xpublic_key=xpublic_key)

bip44_derivation: BIP44Derivation = BIP44Derivation(
    coin_type=Cardano.COIN_TYPE, account=0, change=CHANGES.EXTERNAL_CHAIN, address=0
)
cardano_hd.from_derivation(derivation=bip44_derivation)

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
print("Index:", cardano_hd.index())
print("Indexes:", cardano_hd.indexes())
print("getStrict:", cardano_hd.strict())
print("Address:", cardano_hd.address())
