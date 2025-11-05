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
    BIP84Derivation, CHANGES
)
from hdwallet.hds import BIP84HD


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

# Initialize BIP84 HD
bip84_hd: BIP84HD = BIP84HD(
    ecc=Cryptocurrency.ECC,
    wif_prefix=Cryptocurrency.NETWORKS.MAINNET.WIF_PREFIX,
    coin_type=Cryptocurrency.COIN_TYPE,
    account=0,
    change=CHANGES.EXTERNAL_CHAIN,
    address=0
)
# Update BIP84 HD root keys from seed
bip84_hd.from_seed(
    seed=bip39_seed
)

# Dump root keys
print("BIP84 Seed:", bip84_hd.seed())
print("BIP84 Root XPrivate Key:", bip84_hd.root_xprivate_key())
print("BIP84 Root XPublic Key:", bip84_hd.root_xpublic_key())
print("BIP84 Root Private Key:", bip84_hd.root_private_key())
print("BIP84 Root Chain Code:", bip84_hd.root_chain_code())
print("BIP84 Root Public Key:", bip84_hd.root_public_key())

# Initialize BIP84 derivation
bip84_derivation: BIP84Derivation = BIP84Derivation(
    coin_type=Cryptocurrency.COIN_TYPE
)
bip84_derivation.from_account(account=0)
bip84_derivation.from_change(change=CHANGES.INTERNAL_CHAIN)
bip84_derivation.from_address(address=0)

# Update current BIP84 HD derivation
bip84_hd.from_derivation(
    derivation=bip84_derivation
)
# Or update current BIP84 HD derivation by changing indexes
# bip84_hd.from_coin_type(coin_type=Cryptocurrency.COIN_TYPE)
# bip84_hd.from_account(account=0)
# bip84_hd.from_change(change=CHANGES.INTERNAL_CHAIN)
# bip84_hd.from_address(address=0)

# Dump derived keys
print("BIP84 XPrivate Key:", bip84_hd.xprivate_key())
print("BIP84 XPublic Key:", bip84_hd.xpublic_key())
print("BIP84 Private Key:", bip84_hd.private_key())
print("BIP84 WIF:", bip84_hd.wif())
print("BIP84 Chain Code:", bip84_hd.chain_code())
print("BIP84 Public Key:", bip84_hd.public_key())
print("BIP84 Uncompressed:", bip84_hd.uncompressed())
print("BIP84 Compressed:", bip84_hd.compressed())
print("BIP84 Hash:", bip84_hd.hash())
print("BIP84 Depth:", bip84_hd.depth())
print("BIP84 Path:", bip84_hd.path())
print("BIP84 Index:", bip84_hd.index())
print("BIP84 Indexes:", bip84_hd.indexes())
print("BIP84 Fingerprint:", bip84_hd.fingerprint())
print("BIP84 Parent Fingerprint:", bip84_hd.parent_fingerprint())
print("BIP84 Address:", bip84_hd.address(
    public_key_address_prefix=Cryptocurrency.NETWORKS.MAINNET.PUBLIC_KEY_ADDRESS_PREFIX
))
