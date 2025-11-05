#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.entropies import (
    ElectrumV2Entropy, ELECTRUM_V2_ENTROPY_STRENGTHS
)
from hdwallet.mnemonics import (
    ELECTRUM_V2_MNEMONIC_LANGUAGES, ELECTRUM_V2_MNEMONIC_TYPES
)
from hdwallet.derivations import ElectrumDerivation
from hdwallet.cryptocurrencies import Bitcoin
from hdwallet.consts import (
    MODES, PUBLIC_KEY_TYPES
)
from hdwallet.hds import ElectrumV2HD

import json


hdwallet: HDWallet = HDWallet(
    cryptocurrency=Bitcoin,
    hd=ElectrumV2HD,
    network=Bitcoin.NETWORKS.MAINNET,
    language=ELECTRUM_V2_MNEMONIC_LANGUAGES.PORTUGUESE,
    mnemonic_type=ELECTRUM_V2_MNEMONIC_TYPES.SEGWIT,
    mode=MODES.SEGWIT,
    public_key_type=PUBLIC_KEY_TYPES.UNCOMPRESSED
).from_entropy(
    entropy=ElectrumV2Entropy(
        entropy=ElectrumV2Entropy.generate(
            strength=ELECTRUM_V2_ENTROPY_STRENGTHS.ONE_HUNDRED_THIRTY_TWO
        )
    )
).from_derivation(
    derivation=ElectrumDerivation(
        change=(1, 2), address=(1, 2)
    )
)

# print(json.dumps(hdwallet.dump(), indent=4, ensure_ascii=False))
print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))

# print("Cryptocurrency:", hdwallet.cryptocurrency())
# print("Symbol:", hdwallet.symbol())
# print("Network:", hdwallet.network())
# print("Coin Type:", hdwallet.coin_type())
# print("Entropy:", hdwallet.entropy())
# print("Strength:", hdwallet.strength())
# print("Mnemonic:", hdwallet.mnemonic())
# print("Language:", hdwallet.language())
# print("Seed:", hdwallet.seed())
# print("ECC:", hdwallet.ecc())
# print("HD:", hdwallet.hd())
# print("Mode:", hdwallet.mode())
# print("Mnemonic Type:", hdwallet.mnemonic_type())
# print("Master Private Key:", hdwallet.master_private_key())
# print("Master WIF:", hdwallet.master_wif())
# print("Master Public Key:", hdwallet.master_public_key())
# print("Public Key Type:", hdwallet.public_key_type())
# print("WIF Type:", hdwallet.wif_type())
# print("Private Key:", hdwallet.private_key())
# print("WIF:", hdwallet.wif())
# print("Public Key:", hdwallet.public_key())
# print("Uncompressed:", hdwallet.uncompressed())
# print("Compressed:", hdwallet.compressed())
# print("Address:", hdwallet.address())
