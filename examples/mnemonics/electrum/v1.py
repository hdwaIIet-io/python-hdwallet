#!/usr/bin/env python3

from typing import Type

from hdwallet.mnemonics import (
    MNEMONICS, IMnemonic, ElectrumV1Mnemonic, ELECTRUM_V1_MNEMONIC_LANGUAGES, ELECTRUM_V1_MNEMONIC_WORDS
)

data = {
    "name": "Electrum-V1",
    "entropy": "6304c6da30c9509955cad59983fa8c1e",
    "mnemonic": "bomb physical final feed usually eat mutter stick group shoulder soothe knee",
    "language": ELECTRUM_V1_MNEMONIC_LANGUAGES.ENGLISH,
    "words": ELECTRUM_V1_MNEMONIC_WORDS.TWELVE
}

ElectrumV1MnemonicClass: Type[IMnemonic] = MNEMONICS.mnemonic(data["name"])

electrum_v1_mnemonic_class = ElectrumV1MnemonicClass(data["mnemonic"])
electrum_v1_mnemonic = ElectrumV1Mnemonic(data["mnemonic"])

print(
    electrum_v1_mnemonic_class.mnemonic() == electrum_v1_mnemonic.mnemonic() ==
    ElectrumV1MnemonicClass.from_entropy(data["entropy"], data["language"]) ==
    ElectrumV1Mnemonic.from_entropy(data["entropy"], data["language"]) ==
    data["mnemonic"],

    electrum_v1_mnemonic_class.language() == electrum_v1_mnemonic.language() == data["language"],

    electrum_v1_mnemonic_class.words() == electrum_v1_mnemonic.words() == data["words"],
    ElectrumV1MnemonicClass.is_valid(data["mnemonic"]) == ElectrumV1Mnemonic.is_valid(data["mnemonic"]),

    ElectrumV1MnemonicClass.is_valid_language(data["language"]) == ElectrumV1Mnemonic.is_valid_language(data["language"]),

    ElectrumV1MnemonicClass.is_valid_words(data["words"]) == ElectrumV1Mnemonic.is_valid_words(data["words"]),

    len(ElectrumV1MnemonicClass.from_words(data["words"], data["language"]).split(" ")) ==
    len(ElectrumV1Mnemonic.from_words(data["words"], data["language"]).split(" ")), "\n"
)

print("Client:", data["name"])
print("Mnemonic:", data["mnemonic"])
print("Language:", data["language"])
print("Words:", data["words"])
