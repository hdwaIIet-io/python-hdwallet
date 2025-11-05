#!/usr/bin/env python3

from hdwallet.hds import BIP84HD
from hdwallet.cryptocurrencies import Bitcoin as Cryptocurrency
from hdwallet.derivations import BIP84Derivation, CHANGES
from hdwallet.consts import PUBLIC_KEY_TYPES

bip84_hd: BIP84HD = BIP84HD(
    ecc=Cryptocurrency.ECC,
    public_key_type=PUBLIC_KEY_TYPES.COMPRESSED,
    wif_prefix=Cryptocurrency.NETWORKS.MAINNET.WIF_PREFIX
)

seed = "5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4"
xprivate_key = "xprv9s21ZrQH143K4L18AD5Ko2ELW8bqaGLW4vfASZzo9yEN8fkZPZLdECXWXAMovtonu7DdEFwJuYH31QT96FWJUfkiLUVT8t8e3WNDiwZkuLJ"
xpublic_key = "xpub661MyMwAqRbcGp5bGEcLAAB54ASKyj4MS9amExQQiJmM1U5hw6esmzqzNQtquzBRNvLWtPC2kRu2kZR888FSAiZRpvKdjgbmoKRCgGM1YEy"
private_key = "7f60ec0fa89064a37e208ade560c098586dd887e2133bee4564af1de52bc7f5c"
wif = "L1VKQooPmgVLD35vHMeprus1zFYx58bHGMfTz8QYTEnRCzbjwMoo"
public_key = "023e23967b818fb3959f2056b6e6449a65c4982c1267398d8897b921ab53b0be4b"

bip84_hd.from_seed(seed=seed)
# bip84_hd.from_xprivate_key(xprivate_key=xprivate_key)
# bip84_hd.from_xpublic_key(xpublic_key=xpublic_key)

print("Seed:", bip84_hd.seed())
print("Strict:", bip84_hd.strict())
print("Root XPrivate Key:", bip84_hd.root_xprivate_key())
print("Root XPublic Key:", bip84_hd.root_xpublic_key())
print("Root Private Key:", bip84_hd.root_private_key())
print("Root WIF:", bip84_hd.root_wif())
print("Root Chain Code:", bip84_hd.root_chain_code())
print("Root Public Key:", bip84_hd.root_public_key())

# bip84_derivation: BIP84Derivation = BIP84Derivation(
#     coin_type=Cryptocurrency.COIN_TYPE, account=0, change=CHANGES.EXTERNAL_CHAIN, address=0
# )
# bip84_hd.from_derivation(derivation=bip84_derivation)

bip84_hd.from_coin_type(coin_type=Cryptocurrency.COIN_TYPE)
bip84_hd.from_account(account=0)
bip84_hd.from_change(change=CHANGES.EXTERNAL_CHAIN)
bip84_hd.from_address(address=0)

# bip84_hd.from_private_key(private_key=private_key)
# bip84_hd.from_wif(wif=wif)
# bip84_hd.from_public_key(public_key=public_key)

print("XPrivate Key:", bip84_hd.xprivate_key())
print("XPublic Key:", bip84_hd.xpublic_key())
print("Private Key:", bip84_hd.private_key())
print("WIF:", bip84_hd.wif())
print("WIF Type:", bip84_hd.wif_type())
print("Chain Code:", bip84_hd.chain_code())
print("Public Key:", bip84_hd.public_key())
print("Public Key Type:", bip84_hd.public_key_type())
print("Compressed:", bip84_hd.compressed())
print("Uncompressed:", bip84_hd.uncompressed())
print("Hash:", bip84_hd.hash())
print("Fingerprint:", bip84_hd.fingerprint())
print("Parent Fingerprint:", bip84_hd.parent_fingerprint())
print("Depth:", bip84_hd.depth())
print("Path:", bip84_hd.path())
print("Index:", bip84_hd.index())
print("Indexes:", bip84_hd.indexes())
print("Address:", bip84_hd.address())
