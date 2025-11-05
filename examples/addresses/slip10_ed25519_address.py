#!/usr/bin/env python3

from hdwallet.eccs import (
    IPrivateKey, IPublicKey, SLIP10Ed25519PrivateKey
)
from hdwallet.addresses import (
    AlgorandAddress,
    MultiversXAddress,
    SolanaAddress,
    StellarAddress,
    TezosAddress,
    SuiAddress,
    AptosAddress,
    NearAddress
)
from hdwallet.utils import (
    bytes_to_string, get_bytes
)
from hdwallet.cryptocurrencies import (
    MultiversX, Stellar, Tezos
)

private_key: IPrivateKey = SLIP10Ed25519PrivateKey.from_bytes(get_bytes(
    "bb37794073e5094ebbfcfa070e9254fe6094b56e7cccb094a2304c5eccccdc07"
))
public_key: IPublicKey = private_key.public_key()

print("Private Key:", bytes_to_string(private_key.raw()))
print("Uncompressed Public Key:", bytes_to_string(public_key.raw_uncompressed()))
print("Compressed Public Key:", bytes_to_string(public_key.raw_compressed()), "\n")

algorand_address: str = AlgorandAddress.encode(public_key=public_key)
algorand_public_key: str = AlgorandAddress.decode(address=algorand_address)
print("Algorand Address:", algorand_address, algorand_public_key)

multivers_x_address: str = MultiversXAddress.encode(
    public_key=public_key, hrp=MultiversX.NETWORKS.MAINNET.HRP
)
multivers_x_public_key: str = MultiversXAddress.decode(
    address=multivers_x_address, hrp=MultiversX.NETWORKS.MAINNET.HRP
)
print("MultiversX Address:", multivers_x_address, multivers_x_public_key)

solana_address: str = SolanaAddress.encode(public_key=public_key)
solana_public_key: str = SolanaAddress.decode(address=solana_address)
print("Solana Address:", solana_address, solana_public_key)

stellar_address: str = StellarAddress.encode(
    public_key=public_key, address_type=Stellar.ADDRESS_TYPES.PRIVATE_KEY
)
stellar_public_key: str = StellarAddress.decode(
    address=stellar_address, address_type=Stellar.ADDRESS_TYPES.PRIVATE_KEY
)
print("Stellar Address:", stellar_address, stellar_public_key)

tezos_address: str = TezosAddress.encode(
    public_key=public_key, address_prefix=Tezos.ADDRESS_PREFIXES.TZ1
)
tezos_address_hash: str = TezosAddress.decode(
    address=tezos_address, address_prefix=Tezos.ADDRESS_PREFIXES.TZ1
)
print("Tezos Address:", tezos_address, tezos_address_hash)

sui_address: str = SuiAddress.encode(public_key=public_key)
sui_public_key: str = SuiAddress.decode(address=sui_address)
print("Sui Address:", sui_address, sui_public_key)

aptos_address: str = AptosAddress.encode(public_key=public_key)
aptos_address_hash: str = AptosAddress.decode(address=aptos_address)
print("Aptos Address:", aptos_address, aptos_address_hash)

near_address: str = NearAddress.encode(public_key=public_key)
near_public_key: str = NearAddress.decode(address=near_address)
print("Near Address:", near_address, near_public_key)
