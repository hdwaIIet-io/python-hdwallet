#!/usr/bin/env python3

from typing import Type

from hdwallet.eccs import (
    IEllipticCurveCryptography,
    IPrivateKey,
    IPublicKey,
    IPoint,
    ECCS,
    validate_and_get_public_key,
    SLIP10Ed25519ECC,
    SLIP10Ed25519Point,
    SLIP10Ed25519PublicKey,
    SLIP10Ed25519PrivateKey,
)
from hdwallet.utils import get_bytes, bytes_to_string

ecc: Type[IEllipticCurveCryptography] = ECCS.ecc(SLIP10Ed25519ECC.NAME)

data = {
    "name": "SLIP10-Ed25519",
    "private_key": get_bytes("bb37794073e5094ebbfcfa070e9254fe6094b56e7cccb094a2304c5eccccdc07"),
    "public_key": {
        "uncompressed": get_bytes("00d14696583ee9144878635b557d515a502b04366818dfe7765737746b4f57978d"),
        "compressed": get_bytes("00d14696583ee9144878635b557d515a502b04366818dfe7765737746b4f57978d")
    },
    "point": {
        "raw": get_bytes("d14696583ee9144878635b557d515a502b04366818dfe7765737746b4f57978d"),
        "x": 35008547582340824597639173221735807482318787407965447203743372716499096148063,
        "y": 6147463531448180337884122237947428143499725886130497179241919515820002002641
    }
}

slip10_ed25519_private_key: IPrivateKey = SLIP10Ed25519PrivateKey.from_bytes(data["private_key"])
ecc_slip10_ed25519_private_key: IPrivateKey = ecc.PRIVATE_KEY.from_bytes(data["private_key"])

print(
    "Private Key:",
    ecc.NAME == slip10_ed25519_private_key.name(),
    isinstance(slip10_ed25519_private_key, SLIP10Ed25519PrivateKey),
    isinstance(ecc_slip10_ed25519_private_key, SLIP10Ed25519PrivateKey),
    slip10_ed25519_private_key.raw() == ecc_slip10_ed25519_private_key.raw() == data["private_key"]
)

raw_slip10_ed25519_point: IPoint = SLIP10Ed25519Point.from_bytes(data["point"]["raw"])
coordinates_slip10_ed25519_point: IPoint = SLIP10Ed25519Point.from_coordinates(data["point"]["x"], data["point"]["y"])

print(
    "Point:",
    isinstance(raw_slip10_ed25519_point, SLIP10Ed25519Point),
    isinstance(coordinates_slip10_ed25519_point, SLIP10Ed25519Point),
    raw_slip10_ed25519_point.raw() == coordinates_slip10_ed25519_point.raw() ==
    ecc.POINT.from_bytes(data["point"]["raw"]).raw() ==
    ecc.POINT.from_coordinates(data["point"]["x"], data["point"]["y"]).raw() ==
    data["point"]["raw"]
)

slip10_ed25519_public_key: IPublicKey = slip10_ed25519_private_key.public_key()
ecc_slip10_ed25519_public_key: IPublicKey = ecc_slip10_ed25519_private_key.public_key()
uncompressed_public_key: IPublicKey = validate_and_get_public_key(data["public_key"]["uncompressed"], SLIP10Ed25519PublicKey)
compressed_public_key: IPublicKey = validate_and_get_public_key(data["public_key"]["compressed"], SLIP10Ed25519PublicKey)

print(
    "(Uncompressed) Public Key:",
    isinstance(slip10_ed25519_public_key, SLIP10Ed25519PublicKey),
    isinstance(ecc_slip10_ed25519_public_key, SLIP10Ed25519PublicKey),
    isinstance(uncompressed_public_key, SLIP10Ed25519PublicKey),
    uncompressed_public_key.raw_uncompressed() == slip10_ed25519_public_key.raw_uncompressed() ==
    ecc_slip10_ed25519_public_key.raw_uncompressed() ==
    SLIP10Ed25519PublicKey.from_bytes(data["public_key"]["uncompressed"]).raw_uncompressed() ==
    SLIP10Ed25519PublicKey.from_point(raw_slip10_ed25519_point).raw_uncompressed() ==
    ecc.PUBLIC_KEY.from_bytes(data["public_key"]["uncompressed"]).raw_uncompressed() ==
    ecc.PUBLIC_KEY.from_point(coordinates_slip10_ed25519_point).raw_uncompressed() ==
    data["public_key"]["uncompressed"]
)

print(
    "(Compressed) Public Key:",
    isinstance(slip10_ed25519_public_key, SLIP10Ed25519PublicKey),
    isinstance(ecc_slip10_ed25519_public_key, SLIP10Ed25519PublicKey),
    isinstance(compressed_public_key, SLIP10Ed25519PublicKey),
    compressed_public_key.raw_compressed() == slip10_ed25519_public_key.raw_compressed() ==
    ecc_slip10_ed25519_public_key.raw_compressed() ==
    SLIP10Ed25519PublicKey.from_bytes(data["public_key"]["compressed"]).raw_compressed() ==
    SLIP10Ed25519PublicKey.from_point(raw_slip10_ed25519_point).raw_compressed() ==
    ecc.PUBLIC_KEY.from_bytes(data["public_key"]["compressed"]).raw_compressed() ==
    ecc.PUBLIC_KEY.from_point(coordinates_slip10_ed25519_point).raw_compressed() ==
    data["public_key"]["compressed"]
)

print(
    "ECC:",
    SLIP10Ed25519ECC.NAME == ecc.NAME ==
    slip10_ed25519_private_key.name() == ecc_slip10_ed25519_private_key.name() ==
    raw_slip10_ed25519_point.name() == coordinates_slip10_ed25519_point.name() ==
    slip10_ed25519_public_key.name() == ecc_slip10_ed25519_public_key.name() ==
    data["name"], "\n"
)

print("Elliptic Curve Cryptography:", data["name"])
print("Private Key:", bytes_to_string(data["private_key"]))
print("Point:", bytes_to_string(data["point"]["raw"]))
print("    x:", data["point"]["x"])
print("    y:", data["point"]["y"])
print("(Uncompressed) Public Key:", bytes_to_string(data["public_key"]["uncompressed"]))
print("(Compressed) Public Key:", bytes_to_string(data["public_key"]["compressed"]))
