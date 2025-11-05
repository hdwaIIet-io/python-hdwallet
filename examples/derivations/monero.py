#!/usr/bin/env python3

from hdwallet.derivations import (
    DERIVATIONS, MoneroDerivation
)

data = {
    "name": "Monero",
    "minor": 67,
    "major": 77,
    "path": "m/67/77",
    "indexes": [67, 77],
    "depth": 2,
    "derivations": [
        {
            "minor": 67, "major": 77
        },
        {
            "minor": "0-67", "major": "77"
        },
        {
            "minor": (0, 67), "major": "77"
        }
    ],
    "default": {
        "minor": 1,
        "major": 0,
        "path": "m/1/0",
        "indexes": [1, 0],
        "depth": 2
    }
}

MoneroDerivationClass = DERIVATIONS.derivation(data["name"])

for derivation in data["derivations"]:

    monero_derivation_class = MoneroDerivationClass(
        minor=derivation["minor"],
        major=derivation["major"]
    )
    monero_derivation = MoneroDerivation(
        minor=derivation["minor"],
        major=derivation["major"]
    )

    print(
        monero_derivation_class.minor() == monero_derivation.minor() == data["minor"],
        monero_derivation_class.major() == monero_derivation.major() == data["major"],
        monero_derivation_class.path() == monero_derivation.path() == data["path"],
        monero_derivation_class.indexes() == monero_derivation.indexes() == data["indexes"],
        monero_derivation_class.depth() == monero_derivation.depth() == data["depth"]
    )

    monero_derivation_class.clean()
    monero_derivation.clean()

    print(
        monero_derivation_class.minor() == monero_derivation.minor() == data["default"]["minor"],
        monero_derivation_class.major() == monero_derivation.major() == data["default"]["major"],
        monero_derivation_class.path() == monero_derivation.path() == data["default"]["path"],
        monero_derivation_class.indexes() == monero_derivation.indexes() == data["default"]["indexes"],
        monero_derivation_class.depth() == monero_derivation.depth() == data["default"]["depth"]
    )

    monero_derivation_class.from_minor(derivation["minor"])
    monero_derivation.from_minor(derivation["minor"])
    monero_derivation_class.from_major(derivation["major"])
    monero_derivation.from_major(derivation["major"])

    print(
        monero_derivation_class.minor() == monero_derivation.minor() == data["minor"],
        monero_derivation_class.major() == monero_derivation.major() == data["major"],
        monero_derivation_class.path() == monero_derivation.path() == data["path"],
        monero_derivation_class.indexes() == monero_derivation.indexes() == data["indexes"],
        monero_derivation_class.depth() == monero_derivation.depth() == data["depth"], "\n"
    )

print("Minor:", data["minor"])
print("Major:", data["major"], "\n")

print("Path:", data["path"])
print("Indexes:", data["indexes"])
print("Depth:", data["depth"])
