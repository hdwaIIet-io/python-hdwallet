#!/usr/bin/env python3

from typing import Type

from hdwallet.entropies import (
    ENTROPIES, IEntropy, ElectrumV2Entropy, ELECTRUM_V2_ENTROPY_STRENGTHS
)

data = {
    "name": "Electrum-V2",
    "entropy": "eeeb82d2511334ec979c2b90bcf9803ead7cdd38d690bf8f3723013fa58d42fa44",
    "strength": ELECTRUM_V2_ENTROPY_STRENGTHS.TWO_HUNDRED_SIXTY_FOUR
}

ElectrumV2EntropyClass: Type[IEntropy] = ENTROPIES.entropy(data["name"])

electrum_v2_entropy_class = ElectrumV2EntropyClass(data["entropy"])
electrum_v2_entropy = ElectrumV2Entropy(data["entropy"])

print(
    electrum_v2_entropy_class.strength() == electrum_v2_entropy.strength() == data["strength"],
    electrum_v2_entropy_class.entropy() == electrum_v2_entropy.entropy() == data["entropy"],
    ElectrumV2EntropyClass.is_valid_strength(data["strength"]) == ElectrumV2Entropy.is_valid_strength(data["strength"]),
    ElectrumV2EntropyClass.is_valid(data["entropy"]) == ElectrumV2Entropy.is_valid(data["entropy"]),
    len(ElectrumV2EntropyClass.generate(data["strength"])) == len(ElectrumV2Entropy.generate(data["strength"])),
    "\n"
)

print("Client:", data["name"])
print("Entropy:", data["entropy"])
print("Strength:", data["strength"])
