#!/usr/bin/env python3

from typing import Type

from hdwallet.entropies import (
    ENTROPIES, IEntropy, ElectrumV1Entropy, ELECTRUM_V1_ENTROPY_STRENGTHS
)

data = {
    "name": "Electrum-V1",
    "entropy": "129d9b32df4e382c7abb0d059d83b537",
    "strength": ELECTRUM_V1_ENTROPY_STRENGTHS.ONE_HUNDRED_TWENTY_EIGHT
}

ElectrumV1EntropyClass: Type[IEntropy] = ENTROPIES.entropy(data["name"])

electrum_v1_entropy_class = ElectrumV1EntropyClass(data["entropy"])
electrum_v1_entropy = ElectrumV1Entropy(data["entropy"])

print(
    electrum_v1_entropy_class.strength() == electrum_v1_entropy.strength() == data["strength"],
    electrum_v1_entropy_class.entropy() == electrum_v1_entropy.entropy() == data["entropy"],
    ElectrumV1EntropyClass.is_valid_strength(data["strength"]) == ElectrumV1Entropy.is_valid_strength(data["strength"]),
    ElectrumV1EntropyClass.is_valid(data["entropy"]) == ElectrumV1Entropy.is_valid(data["entropy"]),
    len(ElectrumV1EntropyClass.generate(data["strength"])) == len(ElectrumV1Entropy.generate(data["strength"])),
    "\n"
)

print("Client:", data["name"])
print("Entropy:", data["entropy"])
print("Strength:", data["strength"])
