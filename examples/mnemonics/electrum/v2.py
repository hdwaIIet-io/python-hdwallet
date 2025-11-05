#!/usr/bin/env python3

from typing import Type

from hdwallet.mnemonics import (
    MNEMONICS,
    IMnemonic,
    ElectrumV2Mnemonic,
    ELECTRUM_V2_MNEMONIC_LANGUAGES,
    ELECTRUM_V2_MNEMONIC_WORDS,
    ELECTRUM_V2_MNEMONIC_TYPES
)

data = {
    "name": "Electrum-V2",
    "entropy": "ccc4c46b09115cf2ae02d6301cf2291374908fd14aaed8f5feac21953f669dbe6c",
    "language": ELECTRUM_V2_MNEMONIC_LANGUAGES.ENGLISH,
    "words": ELECTRUM_V2_MNEMONIC_WORDS.TWENTY_FOUR,
    "mnemonics": [
        {
            "mnemonic": "carpet jacket rebuild fault drip prison quiz suggest fiction early elevator empower cheap medal travel copy food retreat junk beyond banana bracket change smoke",
            "mnemonicType": ELECTRUM_V2_MNEMONIC_TYPES.STANDARD
        },
        {
            "mnemonic": "spring ivory rebuild fault drip prison quiz suggest fiction early elevator empower cheap medal travel copy food retreat junk beyond banana bracket change smoke",
            "mnemonicType": ELECTRUM_V2_MNEMONIC_TYPES.SEGWIT
        },
        {
            "mnemonic": "zoo ivory rebuild fault drip prison quiz suggest fiction early elevator empower cheap medal travel copy food retreat junk beyond banana bracket change smoke",
            "mnemonicType": ELECTRUM_V2_MNEMONIC_TYPES.STANDARD_2FA
        },
        {
            "mnemonic": "crawl jacket rebuild fault drip prison quiz suggest fiction early elevator empower cheap medal travel copy food retreat junk beyond banana bracket change smoke",
            "mnemonicType": ELECTRUM_V2_MNEMONIC_TYPES.SEGWIT_2FA
        }
    ]
}

ElectrumV2MnemonicClass: Type[IMnemonic] = MNEMONICS.mnemonic(data["name"])

for mnemonic in data["mnemonics"]:
    electrum_v2_mnemonic_class = ElectrumV2MnemonicClass(mnemonic["mnemonic"], mnemonic_type=mnemonic["mnemonicType"])
    electrum_v2_mnemonic = ElectrumV2Mnemonic(mnemonic["mnemonic"], mnemonic_type=mnemonic["mnemonicType"])

    print(
        electrum_v2_mnemonic_class.mnemonic() == electrum_v2_mnemonic.mnemonic() ==
        ElectrumV2MnemonicClass.from_entropy(data["entropy"], data["language"], mnemonic_type=mnemonic["mnemonicType"]) ==
        ElectrumV2Mnemonic.from_entropy(data["entropy"], data["language"], mnemonic_type=mnemonic["mnemonicType"]) ==
        mnemonic["mnemonic"],

        electrum_v2_mnemonic_class.language() == electrum_v2_mnemonic.language() == data["language"],

        electrum_v2_mnemonic_class.words() == electrum_v2_mnemonic.words() == data["words"],

        electrum_v2_mnemonic_class.mnemonic_type() == electrum_v2_mnemonic.mnemonic_type() == mnemonic["mnemonicType"],

        ElectrumV2MnemonicClass.is_valid(mnemonic["mnemonic"], mnemonic_type=mnemonic["mnemonicType"]) ==
        ElectrumV2Mnemonic.is_valid(mnemonic["mnemonic"], mnemonic_type=mnemonic["mnemonicType"]),

        ElectrumV2MnemonicClass.is_valid_language(data["language"]) == ElectrumV2Mnemonic.is_valid_language(data["language"]),

        ElectrumV2MnemonicClass.is_valid_words(data["words"]) == ElectrumV2Mnemonic.is_valid_words(data["words"]),

        len(ElectrumV2MnemonicClass.from_words(data["words"], data["language"]).split(" ")) ==
        len(ElectrumV2Mnemonic.from_words(data["words"], data["language"]).split(" ")), "\n"
    )

    print("Client:", data["name"])
    print("Mnemonic:", mnemonic["mnemonic"])
    print("Language:", data["language"])
    print("Words:", data["words"])
    print("Mnemonic Type:", mnemonic["mnemonicType"], "\n")
