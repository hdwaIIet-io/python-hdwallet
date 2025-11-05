#!/usr/bin/env python3

from typing import Type

from hdwallet.seeds import (
  SEEDS, ISeed, AlgorandSeed
)

data = {
    "name": "Algorand",
    "mnemonic": "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon invest",
    "seed": "0000000000000000000000000000000000000000000000000000000000000000"
}

AlgorandSeedClass: Type[ISeed] = SEEDS.seed(data["name"])

algorand_seed_class = AlgorandSeedClass(data["seed"])
algorand_seed = AlgorandSeed(data["seed"])

print(
    algorand_seed_class.seed() == algorand_seed.seed() ==
    AlgorandSeedClass.from_mnemonic(data["mnemonic"]) ==
    AlgorandSeed.from_mnemonic(data["mnemonic"]) ==
    data["seed"], "\n"
)

print("Client:", data["name"])
print("Mnemonic:", data["mnemonic"])
print("Seed:", data["seed"])
