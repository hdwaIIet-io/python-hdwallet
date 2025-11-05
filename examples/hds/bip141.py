#!/usr/bin/env python3

from hdwallet.hds import BIP141HD
from hdwallet.cryptocurrencies import Bitcoin as Cryptocurrency
from hdwallet.derivations import CustomDerivation
from hdwallet.consts import PUBLIC_KEY_TYPES, SEMANTICS

bip141_hd: BIP141HD = BIP141HD(
    ecc=Cryptocurrency.ECC,
    public_key_type=PUBLIC_KEY_TYPES.COMPRESSED,
    wif_prefix=Cryptocurrency.NETWORKS.MAINNET.WIF_PREFIX,
    semantic=SEMANTICS.P2WSH_IN_P2SH
)

# bip141_hd.from_semantic(semantic=SEMANTICS.P2WSH_IN_P2SH)

seed = "5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4"
xprivate_key = "xprv9s21ZrQH143K4L18AD5Ko2ELW8bqaGLW4vfASZzo9yEN8fkZPZLdECXWXAMovtonu7DdEFwJuYH31QT96FWJUfkiLUVT8t8e3WNDiwZkuLJ"
xpublic_key = "xpub661MyMwAqRbcGp5bGEcLAAB54ASKyj4MS9amExQQiJmM1U5hw6esmzqzNQtquzBRNvLWtPC2kRu2kZR888FSAiZRpvKdjgbmoKRCgGM1YEy"
wif = "L1VKQooPmgVLD35vHMeprus1zFYx58bHGMfTz8QYTEnRCzbjwMoo"
private_key = "7f60ec0fa89064a37e208ade560c098586dd887e2133bee4564af1de52bc7f5c"
public_key = "023e23967b818fb3959f2056b6e6449a65c4982c1267398d8897b921ab53b0be4b"

bip141_hd.from_seed(seed=seed)
# bip141_hd.from_xprivate_key(xprivate_key=xprivate_key)
# bip141_hd.from_xpublic_key(xpublic_key=xpublic_key)

print("Semantic:", bip141_hd.semantic())
print("Seed:", bip141_hd.seed())
print("Strict:", bip141_hd.strict())
print("Root XPrivate Key:", bip141_hd.root_xprivate_key())
print("Root XPublic Key:", bip141_hd.root_xpublic_key())
print("Root Private Key:", bip141_hd.root_private_key())
print("Root WIF:", bip141_hd.root_wif())
print("Root Chain Code:", bip141_hd.root_chain_code())
print("Root Public Key:", bip141_hd.root_public_key())

custom_derivation: CustomDerivation = CustomDerivation(path="m/0'/0")
bip141_hd.from_derivation(derivation=custom_derivation)

# bip141_hd.from_private_key(private_key=private_key)
# bip141_hd.from_wif(wif=wif)
# bip141_hd.from_public_key(public_key=public_key)

print("XPrivate Key:", bip141_hd.xprivate_key())
print("XPublic Key:", bip141_hd.xpublic_key())
print("Private Key:", bip141_hd.private_key())
print("WIF:", bip141_hd.wif())
print("WIF Type:", bip141_hd.wif_type())
print("Chain Code:", bip141_hd.chain_code())
print("Public Key:", bip141_hd.public_key())
print("Public Key Type:", bip141_hd.public_key_type())
print("Compressed:", bip141_hd.compressed())
print("Uncompressed:", bip141_hd.uncompressed())
print("Hash:", bip141_hd.hash())
print("Fingerprint:", bip141_hd.fingerprint())
print("Parent Fingerprint:", bip141_hd.parent_fingerprint())
print("Depth:", bip141_hd.depth())
print("Path:", bip141_hd.path())
print("Index:", bip141_hd.index())
print("Indexes:", bip141_hd.indexes())
print("Address:", bip141_hd.address())
