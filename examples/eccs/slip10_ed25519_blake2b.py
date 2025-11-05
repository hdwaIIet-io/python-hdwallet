#!/usr/bin/env python3

from typing import Type

from hdwallet.eccs import (
    IEllipticCurveCryptography,
    IPrivateKey,
    IPublicKey,
    IPoint,
    ECCS,
    validate_and_get_public_key,
    SLIP10Ed25519Blake2bECC,
    SLIP10Ed25519Blake2bPoint,
    SLIP10Ed25519Blake2bPublicKey,
    SLIP10Ed25519Blake2bPrivateKey,
)
from hdwallet.utils import get_bytes, bytes_to_string

ecc: Type[IEllipticCurveCryptography] = ECCS.ecc(SLIP10Ed25519Blake2bECC.NAME)

data = {
    "name": "SLIP10-Ed25519-Blake2b",
    "private_key": get_bytes("bb37794073e5094ebbfcfa070e9254fe6094b56e7cccb094a2304c5eccccdc07"),
    "public_key": {
        "uncompressed": get_bytes("006aea61eeed872052377ab16b0fc5d9b9f142be59ac1488e6610645dedb4da45c"),
        "compressed": get_bytes("006aea61eeed872052377ab16b0fc5d9b9f142be59ac1488e6610645dedb4da45c")
    },
    "point": {
        "raw": get_bytes("6aea61eeed872052377ab16b0fc5d9b9f142be59ac1488e6610645dedb4da45c"),
        "x": 34526911383684683276858239193646482780856061288565130556349790613080323854020,
        "y": 41903082350388909699992468710774256578691651237567681160752376024200799971946
    }
}

slip10_ed25519_blake2b_private_key: IPrivateKey = SLIP10Ed25519Blake2bPrivateKey.from_bytes(data["private_key"])
ecc_slip10_ed25519_blake2b_private_key: IPrivateKey = ecc.PRIVATE_KEY.from_bytes(data["private_key"])

print(
    "Private Key:",
    ecc.NAME == slip10_ed25519_blake2b_private_key.name(),
    isinstance(slip10_ed25519_blake2b_private_key, SLIP10Ed25519Blake2bPrivateKey),
    isinstance(ecc_slip10_ed25519_blake2b_private_key, SLIP10Ed25519Blake2bPrivateKey),
    slip10_ed25519_blake2b_private_key.raw() == ecc_slip10_ed25519_blake2b_private_key.raw() == data["private_key"]
)

raw_slip10_ed25519_blake2b_point: IPoint = SLIP10Ed25519Blake2bPoint.from_bytes(data["point"]["raw"])
coordinates_slip10_ed25519_blake2b_point: IPoint = SLIP10Ed25519Blake2bPoint.from_coordinates(data["point"]["x"], data["point"]["y"])

print(
    "Point:",
    isinstance(raw_slip10_ed25519_blake2b_point, SLIP10Ed25519Blake2bPoint),
    isinstance(coordinates_slip10_ed25519_blake2b_point, SLIP10Ed25519Blake2bPoint),
    raw_slip10_ed25519_blake2b_point.raw() == coordinates_slip10_ed25519_blake2b_point.raw() ==
    ecc.POINT.from_bytes(data["point"]["raw"]).raw() ==
    ecc.POINT.from_coordinates(data["point"]["x"], data["point"]["y"]).raw() ==
    data["point"]["raw"]
)

slip10_ed25519_blake2b_public_key: IPublicKey = slip10_ed25519_blake2b_private_key.public_key()
ecc_slip10_ed25519_blake2b_public_key: IPublicKey = ecc_slip10_ed25519_blake2b_private_key.public_key()
uncompressed_public_key: IPublicKey = validate_and_get_public_key(data["public_key"]["uncompressed"], SLIP10Ed25519Blake2bPublicKey)
compressed_public_key: IPublicKey = validate_and_get_public_key(data["public_key"]["compressed"], SLIP10Ed25519Blake2bPublicKey)

print(
    "(Uncompressed) Public Key:",
    isinstance(slip10_ed25519_blake2b_public_key, SLIP10Ed25519Blake2bPublicKey),
    isinstance(ecc_slip10_ed25519_blake2b_public_key, SLIP10Ed25519Blake2bPublicKey),
    isinstance(uncompressed_public_key, SLIP10Ed25519Blake2bPublicKey),
    uncompressed_public_key.raw_uncompressed() == slip10_ed25519_blake2b_public_key.raw_uncompressed() ==
    ecc_slip10_ed25519_blake2b_public_key.raw_uncompressed() ==
    SLIP10Ed25519Blake2bPublicKey.from_bytes(data["public_key"]["uncompressed"]).raw_uncompressed() ==
    SLIP10Ed25519Blake2bPublicKey.from_point(raw_slip10_ed25519_blake2b_point).raw_uncompressed() ==
    ecc.PUBLIC_KEY.from_bytes(data["public_key"]["uncompressed"]).raw_uncompressed() ==
    ecc.PUBLIC_KEY.from_point(coordinates_slip10_ed25519_blake2b_point).raw_uncompressed() ==
    data["public_key"]["uncompressed"]
)

print(
    "(Compressed) Public Key:",
    isinstance(slip10_ed25519_blake2b_public_key, SLIP10Ed25519Blake2bPublicKey),
    isinstance(ecc_slip10_ed25519_blake2b_public_key, SLIP10Ed25519Blake2bPublicKey),
    isinstance(compressed_public_key, SLIP10Ed25519Blake2bPublicKey),
    compressed_public_key.raw_compressed() == slip10_ed25519_blake2b_public_key.raw_compressed() ==
    ecc_slip10_ed25519_blake2b_public_key.raw_compressed() ==
    SLIP10Ed25519Blake2bPublicKey.from_bytes(data["public_key"]["compressed"]).raw_compressed() ==
    SLIP10Ed25519Blake2bPublicKey.from_point(raw_slip10_ed25519_blake2b_point).raw_compressed() ==
    ecc.PUBLIC_KEY.from_bytes(data["public_key"]["compressed"]).raw_compressed() ==
    ecc.PUBLIC_KEY.from_point(coordinates_slip10_ed25519_blake2b_point).raw_compressed() ==
    data["public_key"]["compressed"]
)

print(
    "ECC:",
    SLIP10Ed25519Blake2bECC.NAME == ecc.NAME ==
    slip10_ed25519_blake2b_private_key.name() == ecc_slip10_ed25519_blake2b_private_key.name() ==
    raw_slip10_ed25519_blake2b_point.name() == coordinates_slip10_ed25519_blake2b_point.name() ==
    slip10_ed25519_blake2b_public_key.name() == ecc_slip10_ed25519_blake2b_public_key.name() ==
    data["name"], "\n"
)

print("Elliptic Curve Cryptography:", data["name"])
print("Private Key:", bytes_to_string(data["private_key"]))
print("Point:", bytes_to_string(data["point"]["raw"]))
print("    x:", data["point"]["x"])
print("    y:", data["point"]["y"])
print("(Uncompressed) Public Key:", bytes_to_string(data["public_key"]["uncompressed"]))
print("(Compressed) Public Key:", bytes_to_string(data["public_key"]["compressed"]))
