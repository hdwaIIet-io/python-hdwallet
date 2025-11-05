#!/usr/bin/env python3

from typing import Type

from hdwallet.eccs import (
    IEllipticCurveCryptography,
    IPrivateKey,
    IPublicKey,
    IPoint,
    ECCS,
    validate_and_get_public_key,
    SLIP10Secp256k1ECC,
    SLIP10Secp256k1Point,
    SLIP10Secp256k1PublicKey,
    SLIP10Secp256k1PrivateKey,
)
from hdwallet.utils import get_bytes, bytes_to_string

ecc: Type[IEllipticCurveCryptography] = ECCS.ecc(SLIP10Secp256k1ECC.NAME)

data = {
    "name": "SLIP10-Secp256k1",
    "private_key": get_bytes("b66022fff8b6322f8b8fa444d6d097457b6b9e7bb05add5b75f9c827df7bd3b6"),
    "public_key": {
        "uncompressed": get_bytes("0474a436044b4904bbd7a074b098d65fad39fc5b66f28da8440f10dbcf86568429aae5b09b4de9cee5d2f9f98044f688aa98f910134a8e87eff28ec5ba35ddf273"),
        "compressed": get_bytes("0374a436044b4904bbd7a074b098d65fad39fc5b66f28da8440f10dbcf86568429")
    },
    "point": {
        "raw": get_bytes("0374a436044b4904bbd7a074b098d65fad39fc5b66f28da8440f10dbcf86568429"),
        "x": 52758426164353529380574599868388529660378638078403259786555024244882051335209,
        "y": 77299011131343534153324845262253313862502891835680337281121079752838774387315
    }
}

slip10_secp256k1_private_key: IPrivateKey = SLIP10Secp256k1PrivateKey.from_bytes(data["private_key"])
ecc_slip10_secp256k1_private_key: IPrivateKey = ecc.PRIVATE_KEY.from_bytes(data["private_key"])

print(
    "Private Key:",
    ecc.NAME == slip10_secp256k1_private_key.name(),
    isinstance(slip10_secp256k1_private_key, SLIP10Secp256k1PrivateKey),
    isinstance(ecc_slip10_secp256k1_private_key, SLIP10Secp256k1PrivateKey),
    slip10_secp256k1_private_key.raw() == ecc_slip10_secp256k1_private_key.raw() == data["private_key"]
)

raw_slip10_secp256k1_point: IPoint = SLIP10Secp256k1Point.from_bytes(data["point"]["raw"])
coordinates_slip10_secp256k1_point: IPoint = SLIP10Secp256k1Point.from_coordinates(data["point"]["x"], data["point"]["y"])

print(
    "Point:",
    isinstance(raw_slip10_secp256k1_point, SLIP10Secp256k1Point),
    isinstance(coordinates_slip10_secp256k1_point, SLIP10Secp256k1Point),
    raw_slip10_secp256k1_point.raw() == coordinates_slip10_secp256k1_point.raw() ==
    ecc.POINT.from_bytes(data["point"]["raw"]).raw() ==
    ecc.POINT.from_coordinates(data["point"]["x"], data["point"]["y"]).raw() ==
    data["point"]["raw"]
)

slip10_secp256k1_public_key: IPublicKey = slip10_secp256k1_private_key.public_key()
ecc_slip10_secp256k1_public_key: IPublicKey = ecc_slip10_secp256k1_private_key.public_key()
uncompressed_public_key: IPublicKey = validate_and_get_public_key(data["public_key"]["uncompressed"], SLIP10Secp256k1PublicKey)
compressed_public_key: IPublicKey = validate_and_get_public_key(data["public_key"]["compressed"], SLIP10Secp256k1PublicKey)

print(
    "(Uncompressed) Public Key:",
    isinstance(slip10_secp256k1_public_key, SLIP10Secp256k1PublicKey),
    isinstance(ecc_slip10_secp256k1_public_key, SLIP10Secp256k1PublicKey),
    isinstance(uncompressed_public_key, SLIP10Secp256k1PublicKey),
    uncompressed_public_key.raw_uncompressed() == slip10_secp256k1_public_key.raw_uncompressed() ==
    ecc_slip10_secp256k1_public_key.raw_uncompressed() ==
    SLIP10Secp256k1PublicKey.from_bytes(data["public_key"]["uncompressed"]).raw_uncompressed() ==
    SLIP10Secp256k1PublicKey.from_point(raw_slip10_secp256k1_point).raw_uncompressed() ==
    ecc.PUBLIC_KEY.from_bytes(data["public_key"]["uncompressed"]).raw_uncompressed() ==
    ecc.PUBLIC_KEY.from_point(coordinates_slip10_secp256k1_point).raw_uncompressed() ==
    data["public_key"]["uncompressed"]
)

print(
    "(Compressed) Public Key:",
    isinstance(slip10_secp256k1_public_key, SLIP10Secp256k1PublicKey),
    isinstance(ecc_slip10_secp256k1_public_key, SLIP10Secp256k1PublicKey),
    isinstance(compressed_public_key, SLIP10Secp256k1PublicKey),
    compressed_public_key.raw_compressed() == slip10_secp256k1_public_key.raw_compressed() ==
    ecc_slip10_secp256k1_public_key.raw_compressed() ==
    SLIP10Secp256k1PublicKey.from_bytes(data["public_key"]["compressed"]).raw_compressed() ==
    SLIP10Secp256k1PublicKey.from_point(raw_slip10_secp256k1_point).raw_compressed() ==
    ecc.PUBLIC_KEY.from_bytes(data["public_key"]["compressed"]).raw_compressed() ==
    ecc.PUBLIC_KEY.from_point(coordinates_slip10_secp256k1_point).raw_compressed() ==
    data["public_key"]["compressed"]
)

print(
    "ECC:",
    SLIP10Secp256k1ECC.NAME == ecc.NAME ==
    slip10_secp256k1_private_key.name() == ecc_slip10_secp256k1_private_key.name() ==
    raw_slip10_secp256k1_point.name() == coordinates_slip10_secp256k1_point.name() ==
    slip10_secp256k1_public_key.name() == ecc_slip10_secp256k1_public_key.name() ==
    data["name"], "\n"
)

print("Elliptic Curve Cryptography:", data["name"])
print("Private Key:", bytes_to_string(data["private_key"]))
print("Point:", bytes_to_string(data["point"]["raw"]))
print("    x:", data["point"]["x"])
print("    y:", data["point"]["y"])
print("(Uncompressed) Public Key:", bytes_to_string(data["public_key"]["uncompressed"]))
print("(Compressed) Public Key:", bytes_to_string(data["public_key"]["compressed"]))
