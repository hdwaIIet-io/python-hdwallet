#!/usr/bin/env python3

from hdwallet.eccs import (
    IPrivateKey, IPublicKey, SLIP10Nist256p1PrivateKey
)
from hdwallet.addresses.neo import NeoAddress
from hdwallet.utils import (
    bytes_to_string, get_bytes
)

private_key: IPrivateKey = SLIP10Nist256p1PrivateKey.from_bytes(get_bytes(
    "be3851aa7822b92deb2f34655e41a40fd510f6cf9aa2a4f0c4d7a4bc81f0ad74"
))
public_key: IPublicKey = private_key.public_key()

print("Private Key:", bytes_to_string(private_key.raw()))
print("Uncompressed Public Key:", bytes_to_string(public_key.raw_uncompressed()))
print("Compressed Public Key:", bytes_to_string(public_key.raw_compressed()), "\n")

neo_address: str = NeoAddress.encode(public_key=public_key)
neo_address_hash: str = NeoAddress.decode(address=neo_address)
print("Neo Address:", neo_address, neo_address_hash)
