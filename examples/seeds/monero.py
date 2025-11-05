#!/usr/bin/env python3

from typing import Type

from hdwallet.seeds import (
    SEEDS, ISeed, MoneroSeed
)

data = {
    "name": "Monero",
    "mnemonic": "abbey abbey abbey abbey abbey abbey abbey abbey abbey abbey abbey abbey abbey abbey abbey abbey abbey abbey abbey abbey abbey abbey abbey abbey",
    "seed": "0000000000000000000000000000000000000000000000000000000000000000"
}

MoneroSeedClass: Type[ISeed] = SEEDS.seed(data["name"])

monero_seed_class = MoneroSeedClass(data["seed"])
monero_seed = MoneroSeed(data["seed"])

print(
    monero_seed_class.seed() == monero_seed.seed() ==
    MoneroSeedClass.from_mnemonic(data["mnemonic"]) ==
    MoneroSeed.from_mnemonic(data["mnemonic"]) ==
    data["seed"], "\n"
)

print("Client:", data["name"])
print("Mnemonic:", data["mnemonic"])
print("Seed:", data["seed"])
