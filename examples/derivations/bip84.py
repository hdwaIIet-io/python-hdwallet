#!/usr/bin/env python3

from hdwallet.cryptocurrencies import Bitcoin
from hdwallet.derivations import (
    DERIVATIONS, BIP84Derivation, CHANGES
)

data = {
    "name": "BIP84",
    "purpose": 84,
    "coin_type": Bitcoin.COIN_TYPE,
    "account": 0,
    "change": CHANGES.EXTERNAL_CHAIN,
    "address": 0,
    "path": "m/84'/0'/0'/0/0",
    "indexes": [2147483732, 2147483648, 2147483648, 0, 0],
    "depth": 5,
    "derivations": [
        {
            "coin_type": Bitcoin.COIN_TYPE, "account": 0, "change": CHANGES.EXTERNAL_CHAIN, "address": 0
        },
        {
            "coin_type": "0", "account": "0", "change": "external-chain", "address": "0"
        },
        {
            "coin_type": 0, "account": "0", "change": 0, "address": "0"
        }
    ],
    "default": {
        "purpose": 84,
        "coin_type": Bitcoin.COIN_TYPE,
        "account": 0,
        "change": CHANGES.EXTERNAL_CHAIN,
        "address": 0,
        "path": "m/84'/0'/0'/0/0",
        "indexes": [2147483732, 2147483648, 2147483648, 0, 0],
        "depth": 5
    }
}

BIP84DerivationClass = DERIVATIONS.derivation(data["name"])

for derivation in data["derivations"]:

    bip84_derivation_class = BIP84DerivationClass(
        coin_type=derivation["coin_type"],
        account=derivation["account"],
        change=derivation["change"],
        address=derivation["address"]
    )
    bip84_derivation = BIP84Derivation(
        coin_type=derivation["coin_type"],
        account=derivation["account"],
        change=derivation["change"],
        address=derivation["address"]
    )

    print(
        bip84_derivation_class.purpose() == bip84_derivation.purpose() == data["purpose"],
        bip84_derivation_class.coin_type() == bip84_derivation.coin_type() == data["coin_type"],
        bip84_derivation_class.account() == bip84_derivation.account() == data["account"],
        bip84_derivation_class.change(name_only=True) == bip84_derivation.change(name_only=True) == data["change"],
        bip84_derivation_class.address() == bip84_derivation.address() == data["address"],
        bip84_derivation_class.path() == bip84_derivation.path() == data["path"],
        bip84_derivation_class.indexes() == bip84_derivation.indexes() == data["indexes"],
        bip84_derivation_class.depth() == bip84_derivation.depth() == data["depth"]
    )

    bip84_derivation_class.clean()
    bip84_derivation.clean()

    print(
        bip84_derivation_class.purpose() == bip84_derivation.purpose() == data["default"]["purpose"],
        bip84_derivation_class.coin_type() == bip84_derivation.coin_type() == data["default"]["coin_type"],
        bip84_derivation_class.account() == bip84_derivation.account() == data["default"]["account"],
        bip84_derivation_class.change(name_only=True) == bip84_derivation.change(name_only=True) == data["default"]["change"],
        bip84_derivation_class.address() == bip84_derivation.address() == data["default"]["address"],
        bip84_derivation_class.path() == bip84_derivation.path() == data["default"]["path"],
        bip84_derivation_class.indexes() == bip84_derivation.indexes() == data["default"]["indexes"],
        bip84_derivation_class.depth() == bip84_derivation.depth() == data["default"]["depth"]
    )

    bip84_derivation_class.from_coin_type(derivation["coin_type"])
    bip84_derivation.from_coin_type(derivation["coin_type"])
    bip84_derivation_class.from_account(derivation["account"])
    bip84_derivation.from_account(derivation["account"])
    bip84_derivation_class.from_change(derivation["change"])
    bip84_derivation.from_change(derivation["change"])
    bip84_derivation_class.from_address(derivation["address"])
    bip84_derivation.from_address(derivation["address"])

    print(
        bip84_derivation_class.purpose() == bip84_derivation.purpose() == data["purpose"],
        bip84_derivation_class.coin_type() == bip84_derivation.coin_type() == data["coin_type"],
        bip84_derivation_class.account() == bip84_derivation.account() == data["account"],
        bip84_derivation_class.change(name_only=True) == bip84_derivation.change(name_only=True) == data["change"],
        bip84_derivation_class.address() == bip84_derivation.address() == data["address"],
        bip84_derivation_class.path() == bip84_derivation.path() == data["path"],
        bip84_derivation_class.indexes() == bip84_derivation.indexes() == data["indexes"],
        bip84_derivation_class.depth() == bip84_derivation.depth() == data["depth"], "\n"
    )

print("Purpose:", data['purpose'])
print("Coin Type:", data['coin_type'])
print("Account:", data['account'])
print("Change:", data['change'])
print("Address:", data['address'], "\n")

print("Path:", data['path'])
print("Indexes:", data['indexes'])
print("Depth:", data['depth'])
