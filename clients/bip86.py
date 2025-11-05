#!/usr/bin/env python3

from hdwallet.entropies.bip39 import (
    BIP39Entropy, BIP39_ENTROPY_STRENGTHS
)
from hdwallet.mnemonics.bip39 import (
    BIP39Mnemonic, BIP39_MNEMONIC_LANGUAGES
)
from hdwallet.seeds.bip39 import BIP39Seed
from hdwallet.cryptocurrencies import Bitcoin as Cryptocurrency
from hdwallet.derivations import (
    BIP86Derivation, CHANGES
)
from hdwallet.hds import BIP86HD


# Generate BIP39 entropy
entropy: str = BIP39Entropy.generate(
    strength=BIP39_ENTROPY_STRENGTHS.ONE_HUNDRED_TWENTY_EIGHT
)
bip39_entropy: BIP39Entropy = BIP39Entropy(entropy=entropy)
print("BIP39 Entropy:", bip39_entropy.entropy())
print("BIP39 Strength:", bip39_entropy.strength())

# Get BIP39 mnemonic
mnemonic: str = BIP39Mnemonic.from_entropy(
    entropy=bip39_entropy, language=BIP39_MNEMONIC_LANGUAGES.CHINESE_TRADITIONAL
)
bip39_mnemonic: BIP39Mnemonic = BIP39Mnemonic(mnemonic=mnemonic)
print("BIP39 Mnemonic:", bip39_mnemonic.mnemonic())
print("BIP39 Language:", bip39_mnemonic.language())
print("BIP39 Words:", bip39_mnemonic.words())

# Get BIP39 seed
seed: str = BIP39Seed.from_mnemonic(
    mnemonic=bip39_mnemonic, passphrase=None
)
bip39_seed: BIP39Seed = BIP39Seed(seed=seed)

# Initialize BIP86 HD
bip86_hd: BIP86HD = BIP86HD(
    ecc=Cryptocurrency.ECC,
    wif_prefix=Cryptocurrency.NETWORKS.MAINNET.WIF_PREFIX,
    coin_type=Cryptocurrency.COIN_TYPE,
    account=0,
    change=CHANGES.EXTERNAL_CHAIN,
    address=0
)
# Update BIP86 HD root keys from seed
bip86_hd.from_seed(
    seed=bip39_seed
)

# Dump root keys
print("BIP86 Seed:", bip86_hd.seed())
print("BIP86 Root XPrivate Key:", bip86_hd.root_xprivate_key())
print("BIP86 Root XPublic Key:", bip86_hd.root_xpublic_key())
print("BIP86 Root Private Key:", bip86_hd.root_private_key())
print("BIP86 Root Chain Code:", bip86_hd.root_chain_code())
print("BIP86 Root Public Key:", bip86_hd.root_public_key())

# Initialize BIP86 derivation
bip86_derivation: BIP86Derivation = BIP86Derivation(
    coin_type=Cryptocurrency.COIN_TYPE
)
bip86_derivation.from_account(account=0)
bip86_derivation.from_change(change=CHANGES.INTERNAL_CHAIN)
bip86_derivation.from_address(address=1)

# Update current BIP86 HD derivation
bip86_hd.from_derivation(
    derivation=bip86_derivation
)
# Or update current BIP86 HD derivation by changing indexes
# bip86_hd.from_coin_type(coin_type=Cryptocurrency.COIN_TYPE)
# bip86_hd.from_account(account=0)
# bip86_hd.from_change(change=CHANGES.INTERNAL_CHAIN)
# bip86_hd.from_address(address=0)

# Dump derived keys
print("BIP86 XPrivate Key:", bip86_hd.xprivate_key())
print("BIP86 XPublic Key:", bip86_hd.xpublic_key())
print("BIP86 Private Key:", bip86_hd.private_key())
print("BIP86 WIF:", bip86_hd.wif())
print("BIP86 Chain Code:", bip86_hd.chain_code())
print("BIP86 Public Key:", bip86_hd.public_key())
print("BIP86 Uncompressed:", bip86_hd.uncompressed())
print("BIP86 Compressed:", bip86_hd.compressed())
print("BIP86 Hash:", bip86_hd.hash())
print("BIP86 Depth:", bip86_hd.depth())
print("BIP86 Path:", bip86_hd.path())
print("BIP86 Index:", bip86_hd.index())
print("BIP86 Indexes:", bip86_hd.indexes())
print("BIP86 Fingerprint:", bip86_hd.fingerprint())
print("BIP86 Parent Fingerprint:", bip86_hd.parent_fingerprint())
print("BIP86 Address:", bip86_hd.address(
    public_key_address_prefix=Cryptocurrency.NETWORKS.MAINNET.PUBLIC_KEY_ADDRESS_PREFIX
))
