#!/usr/bin/env python3

from typing import Type

from hdwallet.entropies import (
    ENTROPIES, IEntropy, BIP39Entropy, BIP39_ENTROPY_STRENGTHS
)

data = {
    "name": "BIP39",
    "entropy": "b66022fff8b6322f8b8fa444d6d097457b6b9e7bb05add5b75f9c827df7bd3b6",
    "strength": BIP39_ENTROPY_STRENGTHS.TWO_HUNDRED_FIFTY_SIX
}

BIP39EntropyClass: Type[IEntropy] = ENTROPIES.entropy(data["name"])

bip39_entropy_class = BIP39EntropyClass(data["entropy"])
bip39_entropy = BIP39Entropy(data["entropy"])

print(
    bip39_entropy_class.strength() == bip39_entropy.strength() == data["strength"],
    bip39_entropy_class.entropy() == bip39_entropy.entropy() == data["entropy"],
    BIP39EntropyClass.is_valid_strength(data["strength"]) == BIP39Entropy.is_valid_strength(data["strength"]),
    BIP39EntropyClass.is_valid(data["entropy"]) == BIP39Entropy.is_valid(data["entropy"]),
    len(BIP39EntropyClass.generate(data["strength"])) == len(BIP39Entropy.generate(data["strength"])),
    "\n"
)

print("Client:", data["name"])
print("Entropy:", data["entropy"])
print("Strength:", data["strength"])
