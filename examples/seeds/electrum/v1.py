#!/usr/bin/env python3

from typing import Type

from hdwallet.seeds import (
    SEEDS, ISeed, ElectrumV1Seed
)

data = {
    "name": "Electrum-V1",
    "mnemonic": "like like like like like like like like like like like like",
    "seed": "7c2548ab89ffea8a6579931611969ffc0ed580ccf6048d4230762b981195abe5"
}

ElectrumV1SeedClass: Type[ISeed] = SEEDS.seed(data["name"])

electrum_v1_seed_class = ElectrumV1SeedClass(data["seed"])
electrum_v1_seed = ElectrumV1Seed(data["seed"])

print(
    electrum_v1_seed_class.seed() == electrum_v1_seed.seed() ==
    ElectrumV1SeedClass.from_mnemonic(data["mnemonic"]) ==
    ElectrumV1Seed.from_mnemonic(data["mnemonic"]) ==
    data["seed"], "\n"
)

print("Client:", data["name"])
print("Mnemonic:", data["mnemonic"])
print("Seed:", data["seed"])
