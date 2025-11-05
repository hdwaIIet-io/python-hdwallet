#!/usr/bin/env python3

from hdwallet.hds import CardanoHD
from hdwallet.derivations import CIP1852Derivation, ROLES
from hdwallet.cryptocurrencies import Cardano

cardano_hd: CardanoHD = CardanoHD(
    cardano_type=Cardano.TYPES.SHELLEY_ICARUS
)

seed = "dd585f208c3adf2726d6437bf5278d05"
passphrase = "talonlab"
xprivate_key = "xprv3QESAWYc9vDdZHc7GX4AJ4mMjpZwYbbJyvi8WdtfbQSfSTL3fxPsEQJnRFuyGD15Q1GCndAmQfRM2bRypVoo1SSuyLAQaKhUuRxCStbeHU6wMCQowdVa22eHFeMCPuNDM6GMFy2CDQ99x2HPSupCtFR"
xpublic_key = "xpub661MyMwAqRbcEcRzkCoVUx3mnm2P2u5zuv9Y6Aa7n1NiRbCBbDgSVrsY5uZurNsLzTanEA7GQg9PivUexXH5yNncFvAzj5VhtNWjbiKH2zz"
private_key = "f0b149fb020a04704f5694312963213803395cce9fdffcafaec958940d763f5a250710ebb9a78197db2a5e318e928bbfb0264d11b2a96fb6dbfcc984f9cb3f05"
public_key = "00f3e17380169d8f7fce1cfacab71db9923c848dd289bbbd4d68c5a19050262643"

cardano_hd.from_seed(seed=seed, passphrase=passphrase)
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
