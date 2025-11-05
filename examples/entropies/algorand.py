#!/usr/bin/env python3

from typing import Type

from hdwallet.entropies import (
    ENTROPIES, IEntropy, AlgorandEntropy, ALGORAND_ENTROPY_STRENGTHS
)

data = {
    "name": "Algorand",
    "entropy": "b66022fff8b6322f8b8fa444d6d097457b6b9e7bb05add5b75f9c827df7bd3b6",
    "strength": ALGORAND_ENTROPY_STRENGTHS.TWO_HUNDRED_FIFTY_SIX
}

AlgorandEntropyClass: Type[IEntropy] = ENTROPIES.entropy(data["name"])

algorand_entropy_class = AlgorandEntropyClass(data["entropy"])
algorand_entropy = AlgorandEntropy(data["entropy"])

print(
    algorand_entropy_class.strength() == algorand_entropy.strength() == data["strength"],
    algorand_entropy_class.entropy() == algorand_entropy.entropy() == data["entropy"],
    AlgorandEntropyClass.is_valid_strength(data["strength"]) == AlgorandEntropy.is_valid_strength(data["strength"]),
    AlgorandEntropyClass.is_valid(data["entropy"]) == AlgorandEntropy.is_valid(data["entropy"]),
    len(AlgorandEntropyClass.generate(data["strength"])) == len(AlgorandEntropy.generate(data["strength"])),
    "\n"
)

print("Client:", data["name"])
print("Entropy:", data["entropy"])
print("Strength:", data["strength"])
