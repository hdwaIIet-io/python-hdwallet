#!/usr/bin/env python3

from hdwallet.cryptocurrencies import Qtum
from hdwallet.derivations import (
    DERIVATIONS, BIP49Derivation, CHANGES
)

data = {
    "name": "BIP49",
    "purpose": 49,
    "coin_type": Qtum.COIN_TYPE,
    "account": 0,
    "change": CHANGES.EXTERNAL_CHAIN,
    "address": 0,
    "path": "m/49'/2301'/0'/0/0",
    "indexes": [2147483697, 2147485949, 2147483648, 0, 0],
    "depth": 5,
    "derivations": [
        {
            "coin_type": Qtum.COIN_TYPE, "account": 0, "change": CHANGES.EXTERNAL_CHAIN, "address": 0
        },
        {
            "coin_type": "2301", "account": "0", "change": "external-chain", "address": "0"
        },
        {
            "coin_type": 2301, "account": "0", "change": 0, "address": "0"
        }
    ],
    "default": {
        "purpose": 49,
        "coin_type": Qtum.COIN_TYPE,
        "account": 0,
        "change": CHANGES.EXTERNAL_CHAIN,
        "address": 0,
        "path": "m/49'/2301'/0'/0/0",
        "indexes": [2147483697, 2147485949, 2147483648, 0, 0],
        "depth": 5
    }
}

BIP49DerivationClass = DERIVATIONS.derivation(data["name"])

for derivation in data["derivations"]:

    bip49_derivation_class = BIP49DerivationClass(
        coin_type=derivation["coin_type"],
        account=derivation["account"],
        change=derivation["change"],
        address=derivation["address"]
    )
    bip49_derivation = BIP49Derivation(
        coin_type=derivation["coin_type"],
        account=derivation["account"],
        change=derivation["change"],
        address=derivation["address"]
    )

    print(
        bip49_derivation_class.purpose() == bip49_derivation.purpose() == data["purpose"],
        bip49_derivation_class.coin_type() == bip49_derivation.coin_type() == data["coin_type"],
        bip49_derivation_class.account() == bip49_derivation.account() == data["account"],
        bip49_derivation_class.change(name_only=True) == bip49_derivation.change(name_only=True) == data["change"],
        bip49_derivation_class.address() == bip49_derivation.address() == data["address"],
        bip49_derivation_class.path() == bip49_derivation.path() == data["path"],
        bip49_derivation_class.indexes() == bip49_derivation.indexes() == data["indexes"],
        bip49_derivation_class.depth() == bip49_derivation.depth() == data["depth"]
    )

    bip49_derivation_class.clean()
    bip49_derivation.clean()

    print(
        bip49_derivation_class.purpose() == bip49_derivation.purpose() == data["default"]["purpose"],
        bip49_derivation_class.coin_type() == bip49_derivation.coin_type() == data["default"]["coin_type"],
        bip49_derivation_class.account() == bip49_derivation.account() == data["default"]["account"],
        bip49_derivation_class.change(name_only=True) == bip49_derivation.change(name_only=True) == data["default"]["change"],
        bip49_derivation_class.address() == bip49_derivation.address() == data["default"]["address"],
        bip49_derivation_class.path() == bip49_derivation.path() == data["default"]["path"],
        bip49_derivation_class.indexes() == bip49_derivation.indexes() == data["default"]["indexes"],
        bip49_derivation_class.depth() == bip49_derivation.depth() == data["default"]["depth"]
    )

    bip49_derivation_class.from_coin_type(derivation["coin_type"])
    bip49_derivation.from_coin_type(derivation["coin_type"])
    bip49_derivation_class.from_account(derivation["account"])
    bip49_derivation.from_account(derivation["account"])
    bip49_derivation_class.from_change(derivation["change"])
    bip49_derivation.from_change(derivation["change"])
    bip49_derivation_class.from_address(derivation["address"])
    bip49_derivation.from_address(derivation["address"])

    print(
        bip49_derivation_class.purpose() == bip49_derivation.purpose() == data["purpose"],
        bip49_derivation_class.coin_type() == bip49_derivation.coin_type() == data["coin_type"],
        bip49_derivation_class.account() == bip49_derivation.account() == data["account"],
        bip49_derivation_class.change(name_only=True) == bip49_derivation.change(name_only=True) == data["change"],
        bip49_derivation_class.address() == bip49_derivation.address() == data["address"],
        bip49_derivation_class.path() == bip49_derivation.path() == data["path"],
        bip49_derivation_class.indexes() == bip49_derivation.indexes() == data["indexes"],
        bip49_derivation_class.depth() == bip49_derivation.depth() == data["depth"], "\n"
    )

print("Purpose:", data['purpose'])
print("Coin Type:", data['coin_type'])
print("Account:", data['account'])
print("Change:", data['change'])
print("Address:", data['address'], "\n")

print("Path:", data['path'])
print("Indexes:", data['indexes'])
print("Depth:", data['depth'])
