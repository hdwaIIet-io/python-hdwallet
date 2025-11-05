#!/usr/bin/env python3

from hdwallet.cryptocurrencies import Ethereum
from hdwallet.derivations import (
    DERIVATIONS, BIP44Derivation, CHANGES
)

data = {
    "name": "BIP44",
    "purpose": 44,
    "coin_type": Ethereum.COIN_TYPE,
    "account": 0,
    "change": CHANGES.EXTERNAL_CHAIN,
    "address": 0,
    "path": "m/44'/60'/0'/0/0",
    "indexes": [2147483692, 2147483708, 2147483648, 0, 0],
    "depth": 5,
    "derivations": [
        {
            "coin_type": Ethereum.COIN_TYPE, "account": 0, "change": CHANGES.EXTERNAL_CHAIN, "address": 0
        },
        {
            "coin_type": "60", "account": "0", "change": "external-chain", "address": "0"
        },
        {
            "coin_type": 60, "account": "0", "change": 0, "address": "0"
        }
    ],
    "default": {
        "purpose": 44,
        "coin_type": Ethereum.COIN_TYPE,
        "account": 0,
        "change": CHANGES.EXTERNAL_CHAIN,
        "address": 0,
        "path": "m/44'/60'/0'/0/0",
        "indexes": [2147483692, 2147483708, 2147483648, 0, 0],
        "depth": 5
    }
}

BIP44DerivationClass = DERIVATIONS.derivation(data["name"])

for derivation in data["derivations"]:

    bip44_derivation_class = BIP44DerivationClass(
        coin_type=derivation["coin_type"],
        account=derivation["account"],
        change=derivation["change"],
        address=derivation["address"]
    )
    bip44_derivation = BIP44Derivation(
        coin_type=derivation["coin_type"],
        account=derivation["account"],
        change=derivation["change"],
        address=derivation["address"]
    )

    print(
        bip44_derivation_class.purpose() == bip44_derivation.purpose() == data["purpose"],
        bip44_derivation_class.coin_type() == bip44_derivation.coin_type() == data["coin_type"],
        bip44_derivation_class.account() == bip44_derivation.account() == data["account"],
        bip44_derivation_class.change(name_only=True) == bip44_derivation.change(name_only=True) == data["change"],
        bip44_derivation_class.address() == bip44_derivation.address() == data["address"],
        bip44_derivation_class.path() == bip44_derivation.path() == data["path"],
        bip44_derivation_class.indexes() == bip44_derivation.indexes() == data["indexes"],
        bip44_derivation_class.depth() == bip44_derivation.depth() == data["depth"]
    )

    bip44_derivation_class.clean()
    bip44_derivation.clean()

    print(
        bip44_derivation_class.purpose() == bip44_derivation.purpose() == data["default"]["purpose"],
        bip44_derivation_class.coin_type() == bip44_derivation.coin_type() == data["default"]["coin_type"],
        bip44_derivation_class.account() == bip44_derivation.account() == data["default"]["account"],
        bip44_derivation_class.change(name_only=True) == bip44_derivation.change(name_only=True) == data["default"]["change"],
        bip44_derivation_class.address() == bip44_derivation.address() == data["default"]["address"],
        bip44_derivation_class.path() == bip44_derivation.path() == data["default"]["path"],
        bip44_derivation_class.indexes() == bip44_derivation.indexes() == data["default"]["indexes"],
        bip44_derivation_class.depth() == bip44_derivation.depth() == data["default"]["depth"]
    )

    bip44_derivation_class.from_coin_type(derivation["coin_type"])
    bip44_derivation.from_coin_type(derivation["coin_type"])
    bip44_derivation_class.from_account(derivation["account"])
    bip44_derivation.from_account(derivation["account"])
    bip44_derivation_class.from_change(derivation["change"])
    bip44_derivation.from_change(derivation["change"])
    bip44_derivation_class.from_address(derivation["address"])
    bip44_derivation.from_address(derivation["address"])

    print(
        bip44_derivation_class.purpose() == bip44_derivation.purpose() == data["purpose"],
        bip44_derivation_class.coin_type() == bip44_derivation.coin_type() == data["coin_type"],
        bip44_derivation_class.account() == bip44_derivation.account() == data["account"],
        bip44_derivation_class.change(name_only=True) == bip44_derivation.change(name_only=True) == data["change"],
        bip44_derivation_class.address() == bip44_derivation.address() == data["address"],
        bip44_derivation_class.path() == bip44_derivation.path() == data["path"],
        bip44_derivation_class.indexes() == bip44_derivation.indexes() == data["indexes"],
        bip44_derivation_class.depth() == bip44_derivation.depth() == data["depth"], '\n'
    )

print("Purpose:", data['purpose'])
print("Coin Type:", data['coin_type'])
print("Account:", data['account'])
print("Change:", data['change'])
print("Address:", data['address'], "\n")

print("Path:", data['path'])
print("Indexes:", data['indexes'])
print("Depth:", data['depth'])
