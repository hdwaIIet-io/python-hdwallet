#!/usr/bin/env python3

from hdwallet.derivations import (
    DERIVATIONS, ElectrumDerivation
)

data = {
    "name": "Electrum",
    "change": 10,
    "address": 234234,
    "path": "m/10/234234",
    "indexes": [10, 234234],
    "depth": 2,
    "derivations": [
        {
            "change": 10, "address": 234234
        },
        {
            "change": "0-10", "address": "234234"
        },
        {
            "change": (0, 10), "address": "234234"
        }
    ],
    "default": {
        "change": 0,
        "address": 0,
        "path": "m/0/0",
        "indexes": [0, 0],
        "depth": 2
    }
}

ElectrumDerivationClass = DERIVATIONS.derivation(data["name"])

for derivation in data["derivations"]:

    electrum_derivation_class = ElectrumDerivationClass(
        change=derivation["change"],
        address=derivation["address"]
    )
    electrum_derivation = ElectrumDerivation(
        change=derivation["change"],
        address=derivation["address"]
    )

    print(
        electrum_derivation_class.change() == electrum_derivation.change() == data["change"],
        electrum_derivation_class.address() == electrum_derivation.address() == data["address"],
        electrum_derivation_class.path() == electrum_derivation.path() == data["path"],
        electrum_derivation_class.indexes() == electrum_derivation.indexes() == data["indexes"],
        electrum_derivation_class.depth() == electrum_derivation.depth() == data["depth"]
    )

    electrum_derivation_class.clean()
    electrum_derivation.clean()

    print(
        electrum_derivation_class.change() == electrum_derivation.change() == data["default"]["change"],
        electrum_derivation_class.address() == electrum_derivation.address() == data["default"]["address"],
        electrum_derivation_class.path() == electrum_derivation.path() == data["default"]["path"],
        electrum_derivation_class.indexes() == electrum_derivation.indexes() == data["default"]["indexes"],
        electrum_derivation_class.depth() == electrum_derivation.depth() == data["default"]["depth"]
    )

    electrum_derivation_class.from_change(derivation["change"])
    electrum_derivation.from_change(derivation["change"])
    electrum_derivation_class.from_address(derivation["address"])
    electrum_derivation.from_address(derivation["address"])

    print(
        electrum_derivation_class.change() == electrum_derivation.change() == data["change"],
        electrum_derivation_class.address() == electrum_derivation.address() == data["address"],
        electrum_derivation_class.path() == electrum_derivation.path() == data["path"],
        electrum_derivation_class.indexes() == electrum_derivation.indexes() == data["indexes"],
        electrum_derivation_class.depth() == electrum_derivation.depth() == data["depth"], "\n"
    )

print("Change:", data["change"])
print("Address:", data["address"], "\n")

print("Path:", data["path"])
print("Indexes:", data["indexes"])
print("Depth:", data["depth"])
