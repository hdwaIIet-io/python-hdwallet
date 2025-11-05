#!/usr/bin/env python3

from typing import Type

from hdwallet.mnemonics import ELECTRUM_V2_MNEMONIC_TYPES
from hdwallet.seeds import (
  SEEDS, ISeed, ElectrumV2Seed
)

data = {
    "name": "Electrum-V2",
    "seeds": [
        {
            "mnemonic": "carpet jacket rebuild fault drip prison quiz suggest fiction early elevator empower cheap medal travel copy food retreat junk beyond banana bracket change smoke",
            "seed": "22e0c334cf22eb3c8a93ade2e0d1c43aa979a4426212e6c4099ff4d49434a0c6eecfd1437a79e11ad08605acc94f0255bd77a0728ed9693ab549c385fe610300",
            "mnemonicType": ELECTRUM_V2_MNEMONIC_TYPES.STANDARD
        },
        {
            "mnemonic": "spring ivory rebuild fault drip prison quiz suggest fiction early elevator empower cheap medal travel copy food retreat junk beyond banana bracket change smoke",
            "seed": "cf9d920a1e95f1304ff77d50a15bc06e17eead71947d766780ce9a9ad4efb286e64481542f080c5901a4b3487793a252c5354ab7e6576301a5a08c5b9d771f8a",
            "mnemonicType": ELECTRUM_V2_MNEMONIC_TYPES.SEGWIT
        },
        {
            "mnemonic": "zoo ivory rebuild fault drip prison quiz suggest fiction early elevator empower cheap medal travel copy food retreat junk beyond banana bracket change smoke",
            "seed": "4998375473862dcaf5520afc743980952784ef03d9d1fcec64cb39c25ab38a42c30d6712665408014b5d241abc20b506f1a38bf2adadafedabd97968e3fd8377",
            "mnemonicType": ELECTRUM_V2_MNEMONIC_TYPES.STANDARD_2FA
        },
        {
            "mnemonic": "crawl jacket rebuild fault drip prison quiz suggest fiction early elevator empower cheap medal travel copy food retreat junk beyond banana bracket change smoke",
            "seed": "6abf80ccfa5b8333c0add7d60f53eb0b8c367b09e0693e832c059cc20fe6b1a25d893466255c07241d967ddf2f98fbcd2a838ab3e00073935e8c4714d74caf80",
            "mnemonicType": ELECTRUM_V2_MNEMONIC_TYPES.SEGWIT_2FA
        }
    ]
}

ElectrumV2SeedClass: Type[ISeed] = SEEDS.seed(data["name"])

for seed in data["seeds"]:
    electrum_v2_seed_class = ElectrumV2SeedClass(seed["seed"])
    electrum_v2_seed = ElectrumV2Seed(seed["seed"])

    print(
        electrum_v2_seed_class.seed() == electrum_v2_seed.seed() ==
        ElectrumV2SeedClass.from_mnemonic(seed["mnemonic"], mnemonic_type=seed["mnemonicType"]) ==
        ElectrumV2Seed.from_mnemonic(seed["mnemonic"], mnemonic_type=seed["mnemonicType"]) ==
        seed["seed"], "\n"
    )

    print("Client:", data["name"])
    print("Mnemonic:", seed["mnemonic"])
    print("Seed:", seed["seed"])
    print("Mnemonic Type:", seed["mnemonicType"], "\n")
