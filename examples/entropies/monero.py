#!/usr/bin/env python3

from typing import Type

from hdwallet.entropies import (
    ENTROPIES, IEntropy, MoneroEntropy, MONERO_ENTROPY_STRENGTHS
)

data = {
    "name": "Monero",
    "entropy": "b66022fff8b6322f8b8fa444d6d097457b6b9e7bb05add5b75f9c827df7bd3b6",
    "strength": MONERO_ENTROPY_STRENGTHS.TWO_HUNDRED_FIFTY_SIX
}

MoneroEntropyClass: Type[IEntropy] = ENTROPIES.entropy(data["name"])

monero_entropy_class = MoneroEntropyClass(data["entropy"])
monero_entropy = MoneroEntropy(data["entropy"])

print(
    monero_entropy_class.strength() == monero_entropy.strength() == data["strength"],
    monero_entropy_class.entropy() == monero_entropy.entropy() == data["entropy"],
    MoneroEntropyClass.is_valid_strength(data["strength"]) == MoneroEntropy.is_valid_strength(data["strength"]),
    MoneroEntropyClass.is_valid(data["entropy"]) == MoneroEntropy.is_valid(data["entropy"]),
    len(MoneroEntropyClass.generate(data["strength"])) == len(MoneroEntropy.generate(data["strength"])),
    "\n"
)

print("Client:", data["name"])
print("Entropy:", data["entropy"])
print("Strength:", data["strength"])
