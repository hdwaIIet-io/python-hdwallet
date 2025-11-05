#!/usr/bin/env python3

from typing import Type

from hdwallet.seeds import (
  SEEDS, ISeed, BIP39Seed
)

data = {
    "name": "BIP39",
    "mnemonic": "跡 靈 訟 勾 慌 吞 前 願 詩 奇 希 綱",
    "seeds": [
        {
            "seed": "95ec2455c470704c2a8081324dfecfea53fe4dabac114ad7958b1f4942cd83e10f5f8f1c43ad026a07f3142eeb29dcc72a3b08c6a964904852e6dd3d6945d3b5",
            "passphrase": None
        },
        {
            "seed": "55af5d879d868bdff000e9f9828ac5d5fa95af1552cd0366727acef1e195c870603a336ea3fd502ceb0013617a8fbb3ce99b5a8c0179ec70ce7cbe019245520e",
            "passphrase": "talonlab"
        }
    ]
}

BIP39SeedClass: Type[ISeed] = SEEDS.seed(data["name"])

for seed in data["seeds"]:
    bip39_seed_class = BIP39SeedClass(seed["seed"])
    bip39_seed = BIP39Seed(seed["seed"])

    print(
        bip39_seed_class.seed() == bip39_seed.seed() ==
        BIP39SeedClass.from_mnemonic(data["mnemonic"], passphrase=seed["passphrase"]) ==
        BIP39Seed.from_mnemonic(data["mnemonic"], passphrase=seed["passphrase"]) ==
        seed["seed"], "\n"
    )

    print("Client:", data["name"])
    print("Mnemonic:", data["mnemonic"])
    print("Seed:", BIP39Seed.from_mnemonic(data["mnemonic"], passphrase=seed["passphrase"]))
    print("Passphrase:", seed["passphrase"], "\n")
