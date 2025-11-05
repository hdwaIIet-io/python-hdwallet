    #!/usr/bin/env python3

from hdwallet.eccs import (
    IPrivateKey, IPublicKey, SLIP10Ed25519Blake2bPrivateKey, SLIP10Ed25519Blake2bPublicKey
)
from hdwallet.addresses.nano import NanoAddress
from hdwallet.utils import (
    bytes_to_string, get_bytes
)

private_key: IPrivateKey = SLIP10Ed25519Blake2bPrivateKey.from_bytes(get_bytes(
    "bb37794073e5094ebbfcfa070e9254fe6094b56e7cccb094a2304c5eccccdc07"
))
public_key: IPublicKey = private_key.public_key()

print("Private Key:", bytes_to_string(private_key.raw()))
print("Uncompressed Public Key:", bytes_to_string(public_key.raw_uncompressed()))
print("Compressed Public Key:", bytes_to_string(public_key.raw_compressed()), "\n")

nano_address: str = NanoAddress.encode(
    public_key=public_key
)
nano_public_key: str = NanoAddress.decode(
    address=nano_address
)
print("Nano Address:", nano_address, nano_public_key)
