#!/usr/bin/env python3

from hdwallet.derivations import (
    DERIVATIONS, HDWDerivation
)
from hdwallet.eccs import KholawEd25519ECC

data = {
    "name": "HDW",
    "account": 0,
    "eccs": KholawEd25519ECC.NAME,
    "address": 123,
    "path": "m/0'/3/123",
    "indexes": [2147483648, 3, 123],
    "depth": 3,
    "derivations": [
        {
            "account": 0, "eccs": "Kholaw-Ed25519", "address": (2, 123)
        },
        {
            "account": 0, "eccs": KholawEd25519ECC, "address": 123
        },
        {
            "account": "0", "eccs": "3", "address": "123"
        },
        {
            "account": "0", "eccs": 3, "address": "78-123"
        }
    ],
    "default": {
        "account": 0,
        "eccs": KholawEd25519ECC.NAME,
        "address": 0,
        "path": "m/0'/3/0",
        "indexes": [2147483648, 3, 0],
        "depth": 3
    }
}

HDWDerivationClass = DERIVATIONS.derivation(data["name"])

for derivation in data["derivations"]:

    hdw_derivation_class = HDWDerivationClass(
        account=derivation["account"],
        ecc=derivation["eccs"],
        address=derivation["address"]
    )
    hdw_derivation = HDWDerivation(
        account=derivation["account"],
        ecc=derivation["eccs"],
        address=derivation["address"]
    )

    print(
        hdw_derivation_class.account() == hdw_derivation.account() == data["account"],
        hdw_derivation_class.ecc() == hdw_derivation.ecc() == data["eccs"],
        hdw_derivation_class.address() == hdw_derivation.address() == data["address"],
        hdw_derivation_class.path() == hdw_derivation.path() == data["path"],
        hdw_derivation_class.indexes() == hdw_derivation.indexes() == data["indexes"],
        hdw_derivation_class.depth() == hdw_derivation.depth() == data["depth"]
    )

    hdw_derivation_class.clean()
    hdw_derivation.clean()

    print(
        hdw_derivation_class.account() == hdw_derivation.account() == data["default"]["account"],
        hdw_derivation_class.ecc() == hdw_derivation.ecc() == data["default"]["eccs"],
        hdw_derivation_class.address() == hdw_derivation.address() == data["default"]["address"],
        hdw_derivation_class.path() == hdw_derivation.path() == data["default"]["path"],
        hdw_derivation_class.indexes() == hdw_derivation.indexes() == data["default"]["indexes"],
        hdw_derivation_class.depth() == hdw_derivation.depth() == data["default"]["depth"]
    )

    hdw_derivation_class.from_account(derivation["account"])
    hdw_derivation.from_account(derivation["account"])
    hdw_derivation_class.from_ecc(derivation["eccs"])
    hdw_derivation.from_ecc(derivation["eccs"])
    hdw_derivation_class.from_address(derivation["address"])
    hdw_derivation.from_address(derivation["address"])

    print(
        hdw_derivation_class.account() == hdw_derivation.account() == data["account"],
        hdw_derivation_class.ecc() == hdw_derivation.ecc() == data["eccs"],
        hdw_derivation_class.address() == hdw_derivation.address() == data["address"],
        hdw_derivation_class.path() == hdw_derivation.path() == data["path"],
        hdw_derivation_class.indexes() == hdw_derivation.indexes() == data["indexes"],
        hdw_derivation_class.depth() == hdw_derivation.depth() == data["depth"], '\n'
    )

print("Account:", data["account"])
print("ECC:", data["eccs"])
print("Address:", data["address"], "\n")

print("Path:", data["path"])
print("Indexes:", data["indexes"])
print("Depth:", data["depth"])
