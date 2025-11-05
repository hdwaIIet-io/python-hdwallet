#!/usr/bin/env python3

from hdwallet.entropies import (
    ElectrumV2Entropy, ELECTRUM_V2_ENTROPY_STRENGTHS
)
from hdwallet.mnemonics import (
    ElectrumV2Mnemonic, ELECTRUM_V2_MNEMONIC_LANGUAGES, ELECTRUM_V2_MNEMONIC_TYPES
)
from hdwallet.seeds import ElectrumV2Seed
from hdwallet.hds import ElectrumV2HD
from hdwallet.derivations import ElectrumDerivation
from hdwallet.consts import (
    PUBLIC_KEY_TYPES, MODES
)


# Generate Electrum-V2 entropy
entropy: str = ElectrumV2Entropy.generate(
    strength=ELECTRUM_V2_ENTROPY_STRENGTHS.ONE_HUNDRED_THIRTY_TWO
)
electrum_v2_entropy: ElectrumV2Entropy = ElectrumV2Entropy(entropy=entropy)
print("Electrum-V2 Entropy:", electrum_v2_entropy.entropy())
print("Electrum-V2 Strength:", electrum_v2_entropy.strength())

# Generate Electrum-V2 mnemonic
mnemonic: str = ElectrumV2Mnemonic.from_entropy(
    entropy=electrum_v2_entropy,
    language=ELECTRUM_V2_MNEMONIC_LANGUAGES.ENGLISH,
    mnemonic_type=ELECTRUM_V2_MNEMONIC_TYPES.SEGWIT
)
electrum_v2_mnemonic: ElectrumV2Mnemonic = ElectrumV2Mnemonic(
    mnemonic=mnemonic, mnemonic_type=ELECTRUM_V2_MNEMONIC_TYPES.SEGWIT
)
print("Electrum-V2 Mnemonic:", electrum_v2_mnemonic.mnemonic())
print("Electrum-V2 Language:", electrum_v2_mnemonic.language())
print("Electrum-V2 Words:", electrum_v2_mnemonic.words())
print("Electrum-V2 Mnemonic Type:", electrum_v2_mnemonic.mnemonic_type())

# Get Electrum-V2 seed
seed: str = ElectrumV2Seed.from_mnemonic(
    mnemonic=electrum_v2_mnemonic, mnemonic_type=ELECTRUM_V2_MNEMONIC_TYPES.SEGWIT
)
electrum_v2_seed: ElectrumV2Seed = ElectrumV2Seed(seed=seed)

# Initialize Electrum-V2 HD
electrum_v2_hd: ElectrumV2HD = ElectrumV2HD(
    mode=MODES.SEGWIT, public_key_type=PUBLIC_KEY_TYPES.UNCOMPRESSED
)

# Update Electrum-V2 HD root keys from seed
electrum_v2_hd.from_seed(
    seed=electrum_v2_seed
)

# Dump master keys
print("Electrum-V2 Mode:", electrum_v2_hd.mode())
print("Electrum-V2 Seed:", electrum_v2_hd.seed())
print("Electrum-V2 Master Private Key:", electrum_v2_hd.master_private_key())
print("Electrum-V2 Master WIF:", electrum_v2_hd.master_wif())
print("Electrum-V2 Master Public Key:", electrum_v2_hd.master_public_key())
print("Electrum-V2 Public Key Type:", electrum_v2_hd.public_key_type())
print("Electrum-V2 WIF Type:", electrum_v2_hd.wif_type())

# Initialize Electrum derivation
electrum_derivation: ElectrumDerivation = ElectrumDerivation(
    change=0, address=0
)
# Update current Electrum-V2 HD derivation
electrum_v2_hd.from_derivation(
    derivation=electrum_derivation
)

# Dump derived keys
print("Electrum-V2 Private Key:", electrum_v2_hd.private_key())
print("Electrum-V2 WIF:", electrum_v2_hd.wif())
print("Electrum-V2 Public Key:", electrum_v2_hd.public_key())
print("Electrum-V2 Uncompressed:", electrum_v2_hd.uncompressed())
print("Electrum-V2 Compressed:", electrum_v2_hd.compressed())
print("Electrum-V2 Address:", electrum_v2_hd.address())
