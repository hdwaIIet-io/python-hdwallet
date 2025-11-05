#!/usr/bin/env python3

from hdwallet.derivations import (
    DERIVATIONS, CustomDerivation
)

data = {
    "name": "Custom",
    "path": "m/123'/123'/4'/5/6/7'/8",
    "indexes": [2147483771, 2147483771, 2147483652, 5, 6, 2147483655, 8],
    "depth": 7,
    "default": {
        "path": "m/",
        "indexes": [],
        "depth": 0
    }
}

CustomDerivationClass = DERIVATIONS.derivation(data["name"])

custom_derivation_class = CustomDerivationClass(
    path=data["path"]
)
custom_derivation = CustomDerivation(
    indexes=data["indexes"]
)

print(
    custom_derivation_class.path() == custom_derivation.path() == data["path"],
    custom_derivation_class.indexes() == custom_derivation.indexes() == data["indexes"],
    custom_derivation_class.depth() == custom_derivation.depth() == data["depth"]
)

custom_derivation_class.clean()
custom_derivation.clean()

print(
    custom_derivation_class.path() == custom_derivation.path() == data["default"]["path"],
    custom_derivation_class.indexes() == custom_derivation.indexes() == data["default"]["indexes"],
    custom_derivation_class.depth() == custom_derivation.depth() == data["default"]["depth"]
)

custom_derivation_class.from_path(data["path"])
custom_derivation.from_path(data["path"])

print(
    custom_derivation_class.path() == custom_derivation.path() == data["path"],
    custom_derivation_class.indexes() == custom_derivation.indexes() == data["indexes"],
    custom_derivation_class.depth() == custom_derivation.depth() == data["depth"]
)

custom_derivation_class.clean()
custom_derivation.clean()

custom_derivation_class.from_indexes(data["indexes"])
custom_derivation.from_indexes(data["indexes"])

print(
    custom_derivation_class.path() == custom_derivation.path() == data["path"],
    custom_derivation_class.indexes() == custom_derivation.indexes() == data["indexes"],
    custom_derivation_class.depth() == custom_derivation.depth() == data["depth"]
)

custom_derivation_class.clean()
custom_derivation.clean()

custom_derivation_class.from_index(123, True)
custom_derivation.from_index(123, True)
custom_derivation_class.from_index(123, True)
custom_derivation.from_index(123, True)
custom_derivation_class.from_index(4, True)
custom_derivation.from_index(4, True)
custom_derivation_class.from_index(5)
custom_derivation.from_index(5)
custom_derivation_class.from_index(6)
custom_derivation.from_index(6)
custom_derivation_class.from_index(7, True)
custom_derivation.from_index(7, True)
custom_derivation_class.from_index(8)
custom_derivation.from_index(8)

print(
    custom_derivation_class.path() == custom_derivation.path() == data["path"],
    custom_derivation_class.indexes() == custom_derivation.indexes() == data["indexes"],
    custom_derivation_class.depth() == custom_derivation.depth() == data["depth"], "\n"
)

print("Path:", data["path"])
print("Indexes:", data["indexes"])
print("Depth:", data["depth"])
