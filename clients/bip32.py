#!/usr/bin/env python3

from hdwallet.entropies.bip39 import (
    BIP39Entropy, BIP39_ENTROPY_STRENGTHS
)
from hdwallet.mnemonics.bip39 import (
    BIP39Mnemonic, BIP39_MNEMONIC_LANGUAGES
)
from hdwallet.seeds.bip39 import BIP39Seed
from hdwallet.cryptocurrencies import Bitcoin as Cryptocurrency
from hdwallet.derivations import CustomDerivation
from hdwallet.hds import BIP32HD


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

# Initialize BIP32 HD
bip32_hd: BIP32HD = BIP32HD(
    ecc=Cryptocurrency.ECC, wif_prefix=Cryptocurrency.NETWORKS.MAINNET.WIF_PREFIX
)
# Update BIP32 HD root keys from seed
bip32_hd.from_seed(
    seed=bip39_seed
)

# Dump root keys
print("BIP32 Seed:", bip32_hd.seed())
print("BIP32 Root XPrivate Key:", bip32_hd.root_xprivate_key(
    version=Cryptocurrency.NETWORKS.MAINNET.XPRIVATE_KEY_VERSIONS.P2PKH
))
print("BIP32 Root XPublic Key:", bip32_hd.root_xpublic_key(
    version=Cryptocurrency.NETWORKS.MAINNET.XPUBLIC_KEY_VERSIONS.P2PKH
))
print("BIP32 Root Private Key:", bip32_hd.root_private_key())
print("BIP32 Root Chain Code:", bip32_hd.root_chain_code())
print("BIP32 Root Public Key:", bip32_hd.root_public_key())

# Initialize Custom derivation
custom_derivation: CustomDerivation = CustomDerivation(
    path="m/3215'/7888'/0'/0/0"
)

# Update current BIP32 HD derivation
bip32_hd.from_derivation(
    derivation=custom_derivation
)

# Dump derived keys
print("BIP32 XPrivate Key:", bip32_hd.xprivate_key(
    version=Cryptocurrency.NETWORKS.MAINNET.XPRIVATE_KEY_VERSIONS.P2PKH
))
print("BIP32 XPublic Key:", bip32_hd.xpublic_key(
    version=Cryptocurrency.NETWORKS.MAINNET.XPUBLIC_KEY_VERSIONS.P2PKH
))
print("BIP32 Private Key:", bip32_hd.private_key())
print("BIP32 WIF:", bip32_hd.wif())
print("BIP32 Chain Code:", bip32_hd.chain_code())
print("BIP32 Public Key:", bip32_hd.public_key())
print("BIP32 Uncompressed:", bip32_hd.uncompressed())
print("BIP32 Compressed:", bip32_hd.compressed())
print("BIP32 Hash:", bip32_hd.hash())
print("BIP32 Depth:", bip32_hd.depth())
print("BIP32 Path:", bip32_hd.path())
print("BIP32 Index:", bip32_hd.index())
print("BIP32 Indexes:", bip32_hd.indexes())
print("BIP32 Fingerprint:", bip32_hd.fingerprint())
print("BIP32 Parent Fingerprint:", bip32_hd.parent_fingerprint())
print("BIP32 P2PKH Address:", bip32_hd.address(
    address=Cryptocurrency.ADDRESSES.P2PKH,
    public_key_address_prefix=Cryptocurrency.NETWORKS.MAINNET.PUBLIC_KEY_ADDRESS_PREFIX
))
print("BIP32 P2SH Address:", bip32_hd.address(
    address=Cryptocurrency.ADDRESSES.P2SH,
    script_address_prefix=Cryptocurrency.NETWORKS.MAINNET.SCRIPT_ADDRESS_PREFIX
))
print("BIP32 P2TR Address:", bip32_hd.address(
    address=Cryptocurrency.ADDRESSES.P2TR,
    hrp=Cryptocurrency.NETWORKS.MAINNET.HRP,
    witness_version=Cryptocurrency.NETWORKS.MAINNET.WITNESS_VERSIONS.P2TR
))
print("BIP32 P2WPKH Address:", bip32_hd.address(
    address=Cryptocurrency.ADDRESSES.P2WPKH,
    hrp=Cryptocurrency.NETWORKS.MAINNET.HRP,
    witness_version=Cryptocurrency.NETWORKS.MAINNET.WITNESS_VERSIONS.P2WPKH
))
print("BIP32 P2WPKH-In-P2SH Address:", bip32_hd.address(
    address=Cryptocurrency.ADDRESSES.P2WPKH_IN_P2SH,
    script_address_prefix=Cryptocurrency.NETWORKS.MAINNET.SCRIPT_ADDRESS_PREFIX
))
print("BIP32 P2WSH Address:", bip32_hd.address(
    address=Cryptocurrency.ADDRESSES.P2WSH,
    hrp=Cryptocurrency.NETWORKS.MAINNET.HRP,
    witness_version=Cryptocurrency.NETWORKS.MAINNET.WITNESS_VERSIONS.P2WSH
))
print("BIP32 P2WSH-In-P2SH Address:", bip32_hd.address(
    address=Cryptocurrency.ADDRESSES.P2WSH_IN_P2SH,
    script_address_prefix=Cryptocurrency.NETWORKS.MAINNET.SCRIPT_ADDRESS_PREFIX
))
