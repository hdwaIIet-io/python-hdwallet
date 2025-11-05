#!/usr/bin/env python3

from typing import Type

from hdwallet.eccs import (
    IEllipticCurveCryptography,
    IPrivateKey,
    IPublicKey,
    IPoint,
    ECCS,
    validate_and_get_public_key,
    SLIP10Ed25519MoneroECC,
    SLIP10Ed25519MoneroPoint,
    SLIP10Ed25519MoneroPublicKey,
    SLIP10Ed25519MoneroPrivateKey,
)
from hdwallet.utils import get_bytes, bytes_to_string

ecc: Type[IEllipticCurveCryptography] = ECCS.ecc(SLIP10Ed25519MoneroECC.NAME)

data = {
    "name": "SLIP10-Ed25519-Monero",
    "private_key": get_bytes("bb37794073e5094ebbfcfa070e9254fe6094b56e7cccb094a2304c5eccccdc07"),
    "public_key": {
        "uncompressed": get_bytes("628247d3de93857cdd360fee4aef9a67ecfebedfe8eaec9cf6be35eacc895ca7"),
        "compressed": get_bytes("628247d3de93857cdd360fee4aef9a67ecfebedfe8eaec9cf6be35eacc895ca7")
    },
    "point": {
        "raw": get_bytes("628247d3de93857cdd360fee4aef9a67ecfebedfe8eaec9cf6be35eacc895ca7"),
        "x": 29078407399097928298542937704975150613766572636435642857509307729044618011935,
        "y": 17803702088450816962920827141125906638766406094286540639665541388805331190370
    }
}

slip10_ed25519_monero_private_key: IPrivateKey = SLIP10Ed25519MoneroPrivateKey.from_bytes(data["private_key"])
ecc_slip10_ed25519_monero_private_key: IPrivateKey = ecc.PRIVATE_KEY.from_bytes(data["private_key"])

print(
    "Private Key:",
    ecc.NAME == slip10_ed25519_monero_private_key.name(),
    isinstance(slip10_ed25519_monero_private_key, SLIP10Ed25519MoneroPrivateKey),
    isinstance(ecc_slip10_ed25519_monero_private_key, SLIP10Ed25519MoneroPrivateKey),
    slip10_ed25519_monero_private_key.raw() == ecc_slip10_ed25519_monero_private_key.raw() == data["private_key"]
)

raw_slip10_ed25519_monero_point: IPoint = SLIP10Ed25519MoneroPoint.from_bytes(data["point"]["raw"])
coordinates_slip10_ed25519_monero_point: IPoint = SLIP10Ed25519MoneroPoint.from_coordinates(data["point"]["x"], data["point"]["y"])

print(
    "Point:",
    isinstance(raw_slip10_ed25519_monero_point, SLIP10Ed25519MoneroPoint),
    isinstance(coordinates_slip10_ed25519_monero_point, SLIP10Ed25519MoneroPoint),
    raw_slip10_ed25519_monero_point.raw() == coordinates_slip10_ed25519_monero_point.raw() ==
    ecc.POINT.from_bytes(data["point"]["raw"]).raw() ==
    ecc.POINT.from_coordinates(data["point"]["x"], data["point"]["y"]).raw() ==
    data["point"]["raw"]
)

slip10_ed25519_monero_public_key: IPublicKey = slip10_ed25519_monero_private_key.public_key()
ecc_slip10_ed25519_monero_public_key: IPublicKey = ecc_slip10_ed25519_monero_private_key.public_key()
uncompressed_public_key: IPublicKey = validate_and_get_public_key(data["public_key"]["uncompressed"], SLIP10Ed25519MoneroPublicKey)
compressed_public_key: IPublicKey = validate_and_get_public_key(data["public_key"]["compressed"], SLIP10Ed25519MoneroPublicKey)

print(
    "(Uncompressed) Public Key:",
    isinstance(slip10_ed25519_monero_public_key, SLIP10Ed25519MoneroPublicKey),
    isinstance(ecc_slip10_ed25519_monero_public_key, SLIP10Ed25519MoneroPublicKey),
    isinstance(uncompressed_public_key, SLIP10Ed25519MoneroPublicKey),
    uncompressed_public_key.raw_uncompressed() == slip10_ed25519_monero_public_key.raw_uncompressed() ==
    ecc_slip10_ed25519_monero_public_key.raw_uncompressed() ==
    SLIP10Ed25519MoneroPublicKey.from_bytes(data["public_key"]["uncompressed"]).raw_uncompressed() ==
    SLIP10Ed25519MoneroPublicKey.from_point(raw_slip10_ed25519_monero_point).raw_uncompressed() ==
    ecc.PUBLIC_KEY.from_bytes(data["public_key"]["uncompressed"]).raw_uncompressed() ==
    ecc.PUBLIC_KEY.from_point(coordinates_slip10_ed25519_monero_point).raw_uncompressed() ==
    data["public_key"]["uncompressed"]
)

print(
    "(Compressed) Public Key:",
    isinstance(slip10_ed25519_monero_public_key, SLIP10Ed25519MoneroPublicKey),
    isinstance(ecc_slip10_ed25519_monero_public_key, SLIP10Ed25519MoneroPublicKey),
    isinstance(compressed_public_key, SLIP10Ed25519MoneroPublicKey),
    compressed_public_key.raw_compressed() == slip10_ed25519_monero_public_key.raw_compressed() ==
    ecc_slip10_ed25519_monero_public_key.raw_compressed() ==
    SLIP10Ed25519MoneroPublicKey.from_bytes(data["public_key"]["compressed"]).raw_compressed() ==
    SLIP10Ed25519MoneroPublicKey.from_point(raw_slip10_ed25519_monero_point).raw_compressed() ==
    ecc.PUBLIC_KEY.from_bytes(data["public_key"]["compressed"]).raw_compressed() ==
    ecc.PUBLIC_KEY.from_point(coordinates_slip10_ed25519_monero_point).raw_compressed() ==
    data["public_key"]["compressed"]
)

print(
    "ECC:",
    SLIP10Ed25519MoneroECC.NAME == ecc.NAME ==
    slip10_ed25519_monero_private_key.name() == ecc_slip10_ed25519_monero_private_key.name() ==
    raw_slip10_ed25519_monero_point.name() == coordinates_slip10_ed25519_monero_point.name() ==
    slip10_ed25519_monero_public_key.name() == ecc_slip10_ed25519_monero_public_key.name() ==
    data["name"], "\n"
)

print("Elliptic Curve Cryptography:", data["name"])
print("Private Key:", bytes_to_string(data["private_key"]))
print("Point:", bytes_to_string(data["point"]["raw"]))
print("    x:", data["point"]["x"])
print("    y:", data["point"]["y"])
print("(Uncompressed) Public Key:", bytes_to_string(data["public_key"]["uncompressed"]))
print("(Compressed) Public Key:", bytes_to_string(data["public_key"]["compressed"]))
