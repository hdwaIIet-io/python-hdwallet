#!/usr/bin/env python3

from hdwallet.entropies import (
    ElectrumV1Entropy, ELECTRUM_V1_ENTROPY_STRENGTHS
)
from hdwallet.mnemonics import (
    ElectrumV1Mnemonic, ELECTRUM_V1_MNEMONIC_LANGUAGES
)
from hdwallet.seeds import ElectrumV1Seed
from hdwallet.hds import ElectrumV1HD
from hdwallet.derivations import ElectrumDerivation
from hdwallet.consts import PUBLIC_KEY_TYPES


# Generate Electrum-V1 entropy
entropy: str = ElectrumV1Entropy.generate(
    strength=ELECTRUM_V1_ENTROPY_STRENGTHS.ONE_HUNDRED_TWENTY_EIGHT
)
electrum_v1_entropy: ElectrumV1Entropy = ElectrumV1Entropy(entropy=entropy)
print("Electrum-V1 Entropy:", electrum_v1_entropy.entropy())
print("Electrum-V1 Strength:", electrum_v1_entropy.strength())

# Generate Electrum-V1 mnemonic
mnemonic: str = ElectrumV1Mnemonic.from_entropy(
    entropy=electrum_v1_entropy, language=ELECTRUM_V1_MNEMONIC_LANGUAGES.ENGLISH
)
electrum_v1_mnemonic: ElectrumV1Mnemonic = ElectrumV1Mnemonic(mnemonic=mnemonic)
print("Electrum-V1 Mnemonic:", electrum_v1_mnemonic.mnemonic())
print("Electrum-V1 Language:", electrum_v1_mnemonic.language())
print("Electrum-V1 Words:", electrum_v1_mnemonic.words())

# Get Electrum-V1 seed
seed: str = ElectrumV1Seed.from_mnemonic(
    mnemonic=electrum_v1_mnemonic
)
electrum_v1_seed: ElectrumV1Seed = ElectrumV1Seed(seed=seed)

# Initialize Electrum-V1 HD
electrum_v1_hd: ElectrumV1HD = ElectrumV1HD(
    public_key_type=PUBLIC_KEY_TYPES.COMPRESSED
)

# Update Electrum-V1 HD root keys from seed
electrum_v1_hd.from_seed(
    seed=electrum_v1_seed
)

# Dump master keys
print("Electrum-V2 Seed:", electrum_v1_hd.seed())
print("Electrum-V1 Master Private Key:", electrum_v1_hd.master_private_key())
print("Electrum-V1 Master WIF:", electrum_v1_hd.master_wif())
print("Electrum-V1 Master Public Key:", electrum_v1_hd.master_public_key())
print("Electrum-V1 Public Key Type:", electrum_v1_hd.public_key_type())
print("Electrum-V1 WIF Type:", electrum_v1_hd.wif_type())

# Initialize Electrum derivation
electrum_derivation: ElectrumDerivation = ElectrumDerivation(
    change=0, address=0
)
# Update current Electrum-V1 HD derivation
electrum_v1_hd.from_derivation(
    derivation=electrum_derivation
)

# Dump derived keys
print("Electrum-V1 Private Key:", electrum_v1_hd.private_key())
print("Electrum-V1 WIF:", electrum_v1_hd.wif())
print("Electrum-V1 Public Key:", electrum_v1_hd.public_key())
print("Electrum-V1 Uncompressed:", electrum_v1_hd.uncompressed())
print("Electrum-V1 Compressed:", electrum_v1_hd.compressed())
print("Electrum-V1 Address:", electrum_v1_hd.address())
