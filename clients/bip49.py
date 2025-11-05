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
    BIP49Derivation, CHANGES
)
from hdwallet.hds import BIP49HD


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

# Initialize BIP49 HD
bip49_hd: BIP49HD = BIP49HD(
    ecc=Cryptocurrency.ECC,
    wif_prefix=Cryptocurrency.NETWORKS.MAINNET.WIF_PREFIX,
    coin_type=Cryptocurrency.COIN_TYPE,
    account=0,
    change=CHANGES.EXTERNAL_CHAIN,
    address=0
)
# Update BIP49 HD root keys from seed
bip49_hd.from_seed(
    seed=bip39_seed
)

# Dump root keys
print("BIP49 Seed:", bip49_hd.seed())
print("BIP49 Root XPrivate Key:", bip49_hd.root_xprivate_key())
print("BIP49 Root XPublic Key:", bip49_hd.root_xpublic_key())
print("BIP49 Root Private Key:", bip49_hd.root_private_key())
print("BIP49 Root Chain Code:", bip49_hd.root_chain_code())
print("BIP49 Root Public Key:", bip49_hd.root_public_key())

# Initialize BIP49 derivation
bip49_derivation: BIP49Derivation = BIP49Derivation(
    coin_type=Cryptocurrency.COIN_TYPE
)
bip49_derivation.from_account(account=0)
bip49_derivation.from_change(change=CHANGES.INTERNAL_CHAIN)
bip49_derivation.from_address(address=0)

# Update current BIP49 HD derivation
bip49_hd.from_derivation(
    derivation=bip49_derivation
)
# Or update current BIP49 HD derivation by changing indexes
# bip49_hd.from_coin_type(coin_type=Cryptocurrency.COIN_TYPE)
# bip49_hd.from_account(account=0)
# bip49_hd.from_change(change=CHANGES.INTERNAL_CHAIN)
# bip49_hd.from_address(address=0)

# Dump derived keys
print("BIP49 XPrivate Key:", bip49_hd.xprivate_key())
print("BIP49 XPublic Key:", bip49_hd.xpublic_key())
print("BIP49 Private Key:", bip49_hd.private_key())
print("BIP49 WIF:", bip49_hd.wif())
print("BIP49 Chain Code:", bip49_hd.chain_code())
print("BIP49 Public Key:", bip49_hd.public_key())
print("BIP49 Uncompressed:", bip49_hd.uncompressed())
print("BIP49 Compressed:", bip49_hd.compressed())
print("BIP49 Hash:", bip49_hd.hash())
print("BIP49 Depth:", bip49_hd.depth())
print("BIP49 Path:", bip49_hd.path())
print("BIP49 Index:", bip49_hd.index())
print("BIP49 Indexes:", bip49_hd.indexes())
print("BIP49 Fingerprint:", bip49_hd.fingerprint())
print("BIP49 Parent Fingerprint:", bip49_hd.parent_fingerprint())
print("BIP49 Address:", bip49_hd.address(
    public_key_address_prefix=Cryptocurrency.NETWORKS.MAINNET.PUBLIC_KEY_ADDRESS_PREFIX
))
