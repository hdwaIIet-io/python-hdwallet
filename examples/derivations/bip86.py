#!/usr/bin/env python3

from hdwallet.cryptocurrencies import Qtum
from hdwallet.derivations import (
    DERIVATIONS, BIP86Derivation, CHANGES
)

data = {
    "name": "BIP86",
    "purpose": 86,
    "coin_type": 2301,
    "account": 0,
    "change": CHANGES.INTERNAL_CHAIN,
    "address": 0,
    "path": "m/86'/2301'/0'/1/0",
    "indexes": [2147483734, 2147485949, 2147483648, 1, 0],
    "depth": 5,
    "derivations": [
        {
            "coin_type": Qtum.COIN_TYPE, "account": 0, "change": CHANGES.INTERNAL_CHAIN, "address": 0
        },
        {
            "coin_type": "2301", "account": "0", "change": "internal-chain", "address": "0"
        },
        {
            "coin_type": 2301, "account": "0", "change": 1, "address": "0"
        }
    ],
    "default": {
        "purpose": 86,
        "coin_type": Qtum.COIN_TYPE,
        "account": 0,
        "change": CHANGES.EXTERNAL_CHAIN,
        "address": 0,
        "path": "m/86'/2301'/0'/0/0",
        "indexes": [2147483734, 2147485949, 2147483648, 0, 0],
        "depth": 5
    }
}

BIP86DerivationClass = DERIVATIONS.derivation(data["name"])

for derivation in data["derivations"]:

    bip86_derivation_class = BIP86DerivationClass(
        coin_type=derivation["coin_type"],
        account=derivation["account"],
        change=derivation["change"],
        address=derivation["address"]
    )
    bip86_derivation = BIP86Derivation(
        coin_type=derivation["coin_type"],
        account=derivation["account"],
        change=derivation["change"],
        address=derivation["address"]
    )

    print(
        bip86_derivation_class.purpose() == bip86_derivation.purpose() == data["purpose"],
        bip86_derivation_class.coin_type() == bip86_derivation.coin_type() == data["coin_type"],
        bip86_derivation_class.account() == bip86_derivation.account() == data["account"],
        bip86_derivation_class.change(name_only=True) == bip86_derivation.change(name_only=True) == data["change"],
        bip86_derivation_class.address() == bip86_derivation.address() == data["address"],
        bip86_derivation_class.path() == bip86_derivation.path() == data["path"],
        bip86_derivation_class.indexes() == bip86_derivation.indexes() == data["indexes"],
        bip86_derivation_class.depth() == bip86_derivation.depth() == data["depth"]
    )

    bip86_derivation_class.clean()
    bip86_derivation.clean()

    print(
        bip86_derivation_class.purpose() == bip86_derivation.purpose() == data["default"]["purpose"],
        bip86_derivation_class.coin_type() == bip86_derivation.coin_type() == data["default"]["coin_type"],
        bip86_derivation_class.account() == bip86_derivation.account() == data["default"]["account"],
        bip86_derivation_class.change(name_only=True) == bip86_derivation.change(name_only=True) == data["default"]["change"],
        bip86_derivation_class.address() == bip86_derivation.address() == data["default"]["address"],
        bip86_derivation_class.path() == bip86_derivation.path() == data["default"]["path"],
        bip86_derivation_class.indexes() == bip86_derivation.indexes() == data["default"]["indexes"],
        bip86_derivation_class.depth() == bip86_derivation.depth() == data["default"]["depth"]
    )

    bip86_derivation_class.from_coin_type(derivation["coin_type"])
    bip86_derivation.from_coin_type(derivation["coin_type"])
    bip86_derivation_class.from_account(derivation["account"])
    bip86_derivation.from_account(derivation["account"])
    bip86_derivation_class.from_change(derivation["change"])
    bip86_derivation.from_change(derivation["change"])
    bip86_derivation_class.from_address(derivation["address"])
    bip86_derivation.from_address(derivation["address"])

    print(
        bip86_derivation_class.purpose() == bip86_derivation.purpose() == data["purpose"],
        bip86_derivation_class.coin_type() == bip86_derivation.coin_type() == data["coin_type"],
        bip86_derivation_class.account() == bip86_derivation.account() == data["account"],
        bip86_derivation_class.change(name_only=True) == bip86_derivation.change(name_only=True) == data["change"],
        bip86_derivation_class.address() == bip86_derivation.address() == data["address"],
        bip86_derivation_class.path() == bip86_derivation.path() == data["path"],
        bip86_derivation_class.indexes() == bip86_derivation.indexes() == data["indexes"],
        bip86_derivation_class.depth() == bip86_derivation.depth() == data["depth"], "\n"
    )

print("Purpose:", data['purpose'])
print("Coin Type:", data['coin_type'])
print("Account:", data['account'])
print("Change:", data['change'])
print("Address:", data['address'], "\n")

print("Path:", data['path'])
print("Indexes:", data['indexes'])
print("Depth:", data['depth'])
