#!/usr/bin/env python3

from typing import Type

from hdwallet.mnemonics import (
    MNEMONICS, IMnemonic, AlgorandMnemonic, ALGORAND_MNEMONIC_LANGUAGES, ALGORAND_MNEMONIC_WORDS
)

data = {
    "name": "Algorand",
    "entropy": "b66022fff8b6322f8b8fa444d6d097457b6b9e7bb05add5b75f9c827df7bd3b6",
    "mnemonic": "bitter maze legend hurdle grace slim labor pig silk drive slogan reform street travel long follow knife step lake lady salad ten repair absent sunny",
    "language": ALGORAND_MNEMONIC_LANGUAGES.ENGLISH,
    "words": ALGORAND_MNEMONIC_WORDS.TWENTY_FIVE
}

AlgorandMnemonicClass: Type[IMnemonic] = MNEMONICS.mnemonic(data["name"])

algorand_mnemonic_class = AlgorandMnemonicClass(data["mnemonic"])
algorand_mnemonic = AlgorandMnemonic(data["mnemonic"])

print(
    algorand_mnemonic_class.mnemonic() == algorand_mnemonic.mnemonic() ==
    AlgorandMnemonicClass.from_entropy(data["entropy"], data["language"]) ==
    AlgorandMnemonic.from_entropy(data["entropy"], data["language"]) ==
    data["mnemonic"],

    algorand_mnemonic_class.language() == algorand_mnemonic.language() == data["language"],

    algorand_mnemonic_class.words() == algorand_mnemonic.words() == data["words"],

    AlgorandMnemonicClass.is_valid(data["mnemonic"]) == AlgorandMnemonic.is_valid(data["mnemonic"]),

    AlgorandMnemonicClass.is_valid_language(data["language"]) == AlgorandMnemonic.is_valid_language(data["language"]),

    AlgorandMnemonicClass.is_valid_words(data["words"]) == AlgorandMnemonic.is_valid_words(data["words"]),

    len(AlgorandMnemonicClass.from_words(data["words"], data["language"]).split(" ")) ==
    len(AlgorandMnemonic.from_words(data["words"], data["language"]).split(" ")), "\n"
)

print("Client:", data["name"])
print("Mnemonic:", data["mnemonic"])
print("Language:", data["language"])
print("Words:", data["words"])
