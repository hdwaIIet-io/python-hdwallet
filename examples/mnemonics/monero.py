#!/usr/bin/env python3

from typing import Type

from hdwallet.mnemonics import (
    MNEMONICS, IMnemonic, MoneroMnemonic, MONERO_MNEMONIC_LANGUAGES, MONERO_MNEMONIC_WORDS
)

data = {
    "name": "Monero",
    "entropy": "b66022fff8b6322f8b8fa444d6d097457b6b9e7bb05add5b75f9c827df7bd3b6",
    "language": MONERO_MNEMONIC_LANGUAGES.ENGLISH,
    "mnemonics": [
        {
            "mnemonic": "spying stick spout gimmick tell agony suffice idiom poetry dunes tavern bimonthly fuming seismic eldest wizard utmost fall tanks fitting judge jagged nurse foiled",
            "words": MONERO_MNEMONIC_WORDS.TWENTY_FOUR,
            "checksum": False
        },
        {
            "mnemonic": "spying stick spout gimmick tell agony suffice idiom poetry dunes tavern bimonthly fuming seismic eldest wizard utmost fall tanks fitting judge jagged nurse foiled poetry",
            "words": MONERO_MNEMONIC_WORDS.TWENTY_FIVE,
            "checksum": True
        }
    ]
}

MoneroMnemonicClass: Type[IMnemonic] = MNEMONICS.mnemonic(data["name"])

for mnemonic in data["mnemonics"]:
    monero_mnemonic_class = MoneroMnemonicClass(mnemonic["mnemonic"])
    monero_mnemonic = MoneroMnemonic(mnemonic["mnemonic"])

    print(
        monero_mnemonic_class.mnemonic() == monero_mnemonic.mnemonic() ==
        MoneroMnemonicClass.from_entropy(data["entropy"], data["language"], checksum=mnemonic["checksum"]) ==
        MoneroMnemonic.from_entropy(data["entropy"], data["language"], checksum=mnemonic["checksum"]) ==
        mnemonic["mnemonic"],

        monero_mnemonic_class.language() == monero_mnemonic.language() == data["language"],

        monero_mnemonic_class.words() == monero_mnemonic.words() == mnemonic["words"],

        MoneroMnemonicClass.is_valid(mnemonic["mnemonic"], checksum=mnemonic["checksum"]) ==
        MoneroMnemonic.is_valid(mnemonic["mnemonic"], checksum=mnemonic["checksum"]),

        MoneroMnemonicClass.is_valid_language(data["language"]) == MoneroMnemonic.is_valid_language(data["language"]),

        MoneroMnemonicClass.is_valid_words(mnemonic["words"]) == MoneroMnemonic.is_valid_words(mnemonic["words"]),

        len(MoneroMnemonicClass.from_words(mnemonic["words"], data["language"]).split(" ")) ==
        len(MoneroMnemonic.from_words(mnemonic["words"], data["language"]).split(" ")), "\n"
    )

    print("Client:", data["name"])
    print("Mnemonic:", mnemonic["mnemonic"])
    print("Language:", data["language"])
    print("Words:", mnemonic["words"])
    print("Checksum:", mnemonic["checksum"], "\n")
