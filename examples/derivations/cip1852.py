#!/usr/bin/env python3

from hdwallet.cryptocurrencies import Cardano
from hdwallet.derivations import (
    DERIVATIONS, CIP1852Derivation, ROLES
)

data = {
    "name": "CIP1852",
    "purpose": 1852,
    "coin_type": Cardano.COIN_TYPE,
    "account": 5,
    "role": ROLES.STAKING_KEY,
    "address": 45,
    "path": "m/1852'/1815'/5'/2/45",
    "indexes": [2147485500, 2147485463, 2147483653, 2, 45],
    "depth": 5,
    "derivations": [
        {
            "coin_type": Cardano.COIN_TYPE, "account": 5, "role": ROLES.STAKING_KEY, "address": 45
        },
        {
            "coin_type": "1815", "account": "5", "role": "staking-key", "address": "45"
        },
        {
            "coin_type": 1815, "account": "5", "role": 2, "address": "45"
        }
    ],
    "default": {
        "purpose": 1852,
        "coin_type": Cardano.COIN_TYPE,
        "account": 0,
        "role": ROLES.EXTERNAL_CHAIN,
        "address": 0,
        "path": "m/1852'/1815'/0'/0/0",
        "indexes": [2147485500, 2147485463, 2147483648, 0, 0],
        "depth": 5
    }
}

CIP1852DerivationClass = DERIVATIONS.derivation(data["name"])

for derivation in data["derivations"]:

    cip1852_derivation_class = CIP1852DerivationClass(
        coin_type=derivation["coin_type"],
        account=derivation["account"],
        role=derivation["role"],
        address=derivation["address"]
    )
    cip1852_derivation = CIP1852Derivation(
        coin_type=derivation["coin_type"],
        account=derivation["account"],
        role=derivation["role"],
        address=derivation["address"]
    )

    print(
        cip1852_derivation_class.purpose() == cip1852_derivation.purpose() == data["purpose"],
        cip1852_derivation_class.coin_type() == cip1852_derivation.coin_type() == data["coin_type"],
        cip1852_derivation_class.account() == cip1852_derivation.account() == data["account"],
        cip1852_derivation_class.role() == cip1852_derivation.role() == data["role"],
        cip1852_derivation_class.address() == cip1852_derivation.address() == data["address"],
        cip1852_derivation_class.path() == cip1852_derivation.path() == data["path"],
        cip1852_derivation_class.indexes() == cip1852_derivation.indexes() == data["indexes"],
        cip1852_derivation_class.depth() == cip1852_derivation.depth() == data["depth"]
    )

    cip1852_derivation_class.clean()
    cip1852_derivation.clean()

    print(
        cip1852_derivation_class.purpose() == cip1852_derivation.purpose() == data["default"]["purpose"],
        cip1852_derivation_class.coin_type() == cip1852_derivation.coin_type() == data["default"]["coin_type"],
        cip1852_derivation_class.account() == cip1852_derivation.account() == data["default"]["account"],
        cip1852_derivation_class.role() == cip1852_derivation.role() == data["default"]["role"],
        cip1852_derivation_class.address() == cip1852_derivation.address() == data["default"]["address"],
        cip1852_derivation_class.path() == cip1852_derivation.path() == data["default"]["path"],
        cip1852_derivation_class.indexes() == cip1852_derivation.indexes() == data["default"]["indexes"],
        cip1852_derivation_class.depth() == cip1852_derivation.depth() == data["default"]["depth"]
    )

    cip1852_derivation_class.from_coin_type(derivation["coin_type"])
    cip1852_derivation.from_coin_type(derivation["coin_type"])
    cip1852_derivation_class.from_account(derivation["account"])
    cip1852_derivation.from_account(derivation["account"])
    cip1852_derivation_class.from_role(derivation["role"])
    cip1852_derivation.from_role(derivation["role"])
    cip1852_derivation_class.from_address(derivation["address"])
    cip1852_derivation.from_address(derivation["address"])

    print(
        cip1852_derivation_class.purpose() == cip1852_derivation.purpose() == data["purpose"],
        cip1852_derivation_class.coin_type() == cip1852_derivation.coin_type() == data["coin_type"],
        cip1852_derivation_class.account() == cip1852_derivation.account() == data["account"],
        cip1852_derivation_class.role() == cip1852_derivation.role() == data["role"],
        cip1852_derivation_class.address() == cip1852_derivation.address() == data["address"],
        cip1852_derivation_class.path() == cip1852_derivation.path() == data["path"],
        cip1852_derivation_class.indexes() == cip1852_derivation.indexes() == data["indexes"],
        cip1852_derivation_class.depth() == cip1852_derivation.depth() == data["depth"], "\n"
    )

print("Purpose:", data['purpose'])
print("Coin Type:", data['coin_type'])
print("Account:", data['account'])
print("Role:", data['role'])
print("Address:", data['address'], "\n")

print("Path:", data['path'])
print("Indexes:", data['indexes'])
print("Depth:", data['depth'])
