#!/usr/bin/env python3

from typing import Type

from hdwallet.mnemonics import (
    MNEMONICS, IMnemonic, BIP39Mnemonic, BIP39_MNEMONIC_LANGUAGES, BIP39_MNEMONIC_WORDS
)

data = {
    "name": "BIP39",
    "entropy": "b66022fff8b6322f8b8fa444d6d097457b6b9e7bb05add5b75f9c827df7bd3b6",
    "mnemonic": "reopen absurd say vapor glimpse blind comfort virus dynamic repair chair memory repeat song uphold area tail sweet lazy motion law sadness excite spawn",
    "language": BIP39_MNEMONIC_LANGUAGES.ENGLISH,
    "words": BIP39_MNEMONIC_WORDS.TWENTY_FOUR
}

BIP39MnemonicClass: Type[IMnemonic] = MNEMONICS.mnemonic(data["name"])

bip39_mnemonic_class = BIP39MnemonicClass(data["mnemonic"])
bip39_mnemonic = BIP39Mnemonic(data["mnemonic"])

print(
    bip39_mnemonic_class.mnemonic() == bip39_mnemonic.mnemonic() ==
    BIP39MnemonicClass.from_entropy(data["entropy"], data["language"]) ==
    BIP39Mnemonic.from_entropy(data["entropy"], data["language"]) ==
    data["mnemonic"],

    bip39_mnemonic_class.language() == bip39_mnemonic.language() == data["language"],

    bip39_mnemonic_class.words() == bip39_mnemonic.words() == data["words"],

    BIP39MnemonicClass.is_valid(data["mnemonic"]) == BIP39Mnemonic.is_valid(data["mnemonic"]),

    BIP39MnemonicClass.is_valid_language(data["language"]) == BIP39Mnemonic.is_valid_language(data["language"]),

    BIP39MnemonicClass.is_valid_words(data["words"]) == BIP39Mnemonic.is_valid_words(data["words"]),

    len(BIP39MnemonicClass.from_words(data["words"], data["language"]).split(" ")) ==
    len(BIP39Mnemonic.from_words(data["words"], data["language"]).split(" ")), "\n"
)

print("Client:", data["name"])
print("Mnemonic:", data["mnemonic"])
print("Language:", data["language"])
print("Words:", data["words"])
