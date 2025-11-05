#!/usr/bin/env python3

from hdwallet.cryptocurrencies import Monero
from hdwallet.eccs import (
    SLIP10Ed25519MoneroPrivateKey, SLIP10Ed25519MoneroPublicKey, IPrivateKey, IPublicKey
)

from hdwallet.utils import (
    bytes_to_string, get_bytes
)

from hdwallet.addresses.monero import MoneroAddress

spend_private_key: IPrivateKey = SLIP10Ed25519MoneroPrivateKey.from_bytes(get_bytes(
    "bb37794073e5094ebbfcfa070e9254fe6094b56e7cccb094a2304c5eccccdc07"
))
spend_public_key: IPublicKey = spend_private_key.public_key()
print("Spend Private Key:", bytes_to_string(spend_private_key.raw()))
print("Spend Uncompressed Public Key:", bytes_to_string(spend_public_key.raw_uncompressed()))
print("Spend Compressed Public Key:", bytes_to_string(spend_public_key.raw_compressed()), "\n")

view_private_key: IPrivateKey = SLIP10Ed25519MoneroPrivateKey.from_bytes(get_bytes(
    "e3d2855510a8ecba639c29118719ba895446bedbc80f3527c877de43a8d3cf05"
))
view_public_key: IPublicKey = view_private_key.public_key()
print("View Private Key:", bytes_to_string(view_private_key.raw()))
print("View Uncompressed Public Key:", bytes_to_string(view_public_key.raw_uncompressed()))
print("View Compressed Public Key:", bytes_to_string(view_public_key.raw_compressed()), "\n")

monero_address: str = MoneroAddress.encode(
    spend_public_key=spend_public_key,
    view_public_key=view_public_key,
    network="mainnet",
    address_type = Monero.ADDRESS_TYPES.STANDARD
)
monero_spend_public_key, monero_view_public_key = MoneroAddress.decode(
    address=monero_address,
    network="mainnet",
    address_type = Monero.ADDRESS_TYPES.STANDARD
)
print("Monero Address:", monero_address, (monero_spend_public_key, monero_view_public_key))

