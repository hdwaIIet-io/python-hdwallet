#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.eccs import (
    SLIP10Secp256k1ECC, SLIP10Ed25519ECC
)
from hdwallet.seeds.bip39 import BIP39Seed
from hdwallet.cryptocurrencies import (
    Algorand, Solana, Stellar, Neo
)
from hdwallet.hds import BIP44HD

seed: str = BIP39Seed.from_mnemonic(
    mnemonic="abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about",
    passphrase=None
)

for Cryptocurrency, ECC in [
    (Algorand, SLIP10Ed25519ECC),
    (Solana, Solana.ECC),
    (Stellar, Stellar.ECC),
    (Neo, Neo.ECC)
]:

    bip44_hd: BIP44HD = BIP44HD(
        ecc=SLIP10Secp256k1ECC, coin_type=Cryptocurrency.COIN_TYPE
    ).from_seed(seed=BIP39Seed(seed=seed))

    hdwallet: HDWallet = HDWallet(
        ecc=ECC, cryptocurrency=Cryptocurrency, hd=BIP44HD, network=Cryptocurrency.NETWORKS.MAINNET
    ).from_private_key(
        private_key=bip44_hd.private_key()
    )

    # Same address of Exodus
    print(f"Address for {Cryptocurrency.NAME}: {hdwallet.address()}")
