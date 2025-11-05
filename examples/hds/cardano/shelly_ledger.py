#!/usr/bin/env python3

from hdwallet.hds import CardanoHD
from hdwallet.derivations import CIP1852Derivation, ROLES
from hdwallet.cryptocurrencies import Cardano

cardano_hd: CardanoHD = CardanoHD(
    cardano_type=Cardano.TYPES.SHELLEY_LEDGER
)

seed = "2f370832206daef44362eeb0327f1c04c4e64ce4535754e2d94656f6698382a243393120e71bdf9d4ae4543723aabe8477b20e473c6517b7971cd15a1e760960"
xprivate_key = "xprv3QESAWYc9vDdZnQAzoRU9TqGMCHQsNv54B6ZbYH9XBUxjS8dzG54TAvYnv3LGrxv8JJTA5CwppfcrELdK554QjuKHU678otKHdEUxniPYvXXnv5eaDKmGwEXQq3TwbFfbFJ3Ws5odsquz1PvnDbJ2z6"
xpublic_key = "xpub661MyMwAqRbcGHMw89APz6eSmz7oeCnWTLFtYuoUVaCwvTFHjVYeC79w5fwXsyNcN1GgvnZ6378pUqE2FkteESXiY4LutWk6Xni7fveKg7h"
private_key = "8026b8503b6f07b3b488a89c189353e78fe4034bbe4a0af6cc00bd28dca675404b040c2d196daeb7d1b91f52a986619fa170a73a95ce1dc38d1936d4052f273e"
public_key = "aec80e2cdf3c6d9b8f41a7124017a5507e26ee744c01a931815dcd801575af2d"

cardano_hd.from_seed(seed=seed)
# cardano_hd.from_xprivate_key(xprivate_key=xprivate_key, encoded=True)
# cardano_hd.from_xpublic_key(xpublic_key=xpublic_key, encoded=True)

print("Seed:", cardano_hd.seed())
print("Root XPrivate Key:", cardano_hd.root_xprivate_key())
print("Root XPublic Key:", cardano_hd.root_xpublic_key())
print("Root Private Key:", cardano_hd.root_private_key())
print("Root Chain Code:", cardano_hd.root_chain_code())
print("Root Public Key:", cardano_hd.root_public_key())

cip1852_derivation: CIP1852Derivation = CIP1852Derivation(
    coin_type=Cardano.COIN_TYPE,
    account=0,
    role=ROLES.STAKING_KEY,
    address=0
)

cardano_hd.from_derivation(derivation=cip1852_derivation)

print("Staking XPrivate Key:", cardano_hd.xprivate_key())
print("Staking XPublic Key:", cardano_hd.xpublic_key())
print("Staking Private Key:", cardano_hd.private_key())
print("Staking Chain Code:", cardano_hd.chain_code())
staking_public_key = cardano_hd.public_key()
print("Staking Public Key:", staking_public_key)
print("Staking Public Key Type:", cardano_hd.public_key_type())
print("Staking Compressed:", cardano_hd.compressed())
print("Staking Uncompressed:", cardano_hd.uncompressed())
print("Staking Hash:", cardano_hd.hash())
print("Staking Fingerprint:", cardano_hd.fingerprint())
print("Staking Parent Fingerprint:", cardano_hd.parent_fingerprint())
print("Staking Depth:", cardano_hd.depth())
print("Staking Path:", cardano_hd.path())
print("Staking Index:", cardano_hd.index())
print("Staking Indexes:", cardano_hd.indexes())
print("Staking Strict:", cardano_hd.strict())
print("Staking Address:", cardano_hd.address(
    address_type=Cardano.ADDRESS_TYPES.STAKING
))

cip1852_derivation.from_role(role=ROLES.EXTERNAL_CHAIN)
cardano_hd.update_derivation(derivation=cip1852_derivation)

# cardano_hd.from_private_key(private_key=private_key)
# cardano_hd.from_public_key(public_key=public_key)

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
print("Address:", cardano_hd.address(
    address_type=Cardano.ADDRESS_TYPES.PAYMENT,
    staking_public_key=staking_public_key,
    network="mainnet"
))
