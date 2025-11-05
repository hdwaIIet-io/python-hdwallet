#!/usr/bin/env python3

from hdwallet.hds import AlgorandHD
from hdwallet.cryptocurrencies import Algorand as Cryptocurrency
from hdwallet.derivations import (
    BIP44Derivation, CHANGES
)

algorand_hd: AlgorandHD = AlgorandHD()

seed = "3be138b36c013fc797d9a897dfeb57c82bfa43f32509753140d851bc88be0fbe5a0abe984e0ca0678749952a1b1f99853ce30b0c388a4da38e2a65c5d1f23e9b"
xprivate_key = "xprv9s21ZrQH143K4L18AD5Ko2ELW8bqaGLW4vfASZzo9yEN8fkZPZLdECXWXAMovtonu7DdEFwJuYH31QT96FWJUfkiLUVT8t8e3WNDiwZkuLJ"
xpublic_key = "xpub661MyMwAqRbcGp5bGEcLAAB54ASKyj4MS9amExQQiJmM1U5hw6esmzqzNQtquzBRNvLWtPC2kRu2kZR888FSAiZRpvKdjgbmoKRCgGM1YEy"
private_key = "7f60ec0fa89064a37e208ade560c098586dd887e2133bee4564af1de52bc7f5c"
wif = "L1VKQooPmgVLD35vHMeprus1zFYx58bHGMfTz8QYTEnRCzbjwMoo"
public_key = "023e23967b818fb3959f2056b6e6449a65c4982c1267398d8897b921ab53b0be4b"

algorand_hd.from_seed(seed=seed)
# algorand_hd.from_xprivate_key(xprivate_key=xprivate_key)
# algorand_hd.from_xpublic_key(xpublic_key=xpublic_key)

print("Seed:", algorand_hd.seed())
print("Strict:", algorand_hd.strict())
print("Root XPrivate Key:", algorand_hd.root_xprivate_key())
print("Root XPublic Key:", algorand_hd.root_xpublic_key())
print("Root Private Key:", algorand_hd.root_private_key())
print("Root Chain Code:", algorand_hd.root_chain_code())
print("Root Public Key:", algorand_hd.root_public_key())

bip44_derivation: BIP44Derivation = BIP44Derivation(
    coin_type=Cryptocurrency.COIN_TYPE, account=0, change=CHANGES.EXTERNAL_CHAIN, address=0
)
algorand_hd.from_derivation(derivation=bip44_derivation)

# algorand_hd.from_private_key(private_key=private_key)
# algorand_hd.from_wif(wif=wif)
# algorand_hd.from_public_key(public_key=public_key)

print("XPrivate Key:", algorand_hd.xprivate_key())
print("XPublic Key:", algorand_hd.xpublic_key())
print("Private Key:", algorand_hd.private_key())
print("Chain Code:", algorand_hd.chain_code())
print("Public Key:", algorand_hd.public_key())
print("Hash:", algorand_hd.hash())
print("Fingerprint:", algorand_hd.fingerprint())
print("Parent Fingerprint:", algorand_hd.parent_fingerprint())
print("Depth:", algorand_hd.depth())
print("Path:", algorand_hd.path())
print("Index:", algorand_hd.index())
print("Indexes:", algorand_hd.indexes())
print("Address:", algorand_hd.address())
