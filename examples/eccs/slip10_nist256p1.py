#!/usr/bin/env python3

from typing import Type

from hdwallet.eccs import (
    IEllipticCurveCryptography,
    IPrivateKey,
    IPublicKey,
    IPoint,
    ECCS,
    validate_and_get_public_key,
    SLIP10Nist256p1ECC,
    SLIP10Nist256p1Point,
    SLIP10Nist256p1PublicKey,
    SLIP10Nist256p1PrivateKey,
)
from hdwallet.utils import get_bytes, bytes_to_string

ecc: Type[IEllipticCurveCryptography] = ECCS.ecc(SLIP10Nist256p1ECC.NAME)

data = {
    "name": "SLIP10-Nist256p1",
    "private_key": get_bytes("f79495fda777197ce73551bcd8e162ceca19167575760d3cc2bced4bf2a213dc"),
    "public_key": {
        "uncompressed": get_bytes("04e4bd97a82a8f3e575a9a35b7cca19cd730addd499a2bd4e9a9811df8bfc35e51c68c3bed41d47d4d05ae880250e4432cc6480b417597f1cffc5ed7d28991d164"),
        "compressed": get_bytes("02e4bd97a82a8f3e575a9a35b7cca19cd730addd499a2bd4e9a9811df8bfc35e51")
    },
    "point": {
        "raw": get_bytes("02e4bd97a82a8f3e575a9a35b7cca19cd730addd499a2bd4e9a9811df8bfc35e51"),
        "x": 103462310269679299860340333843259692621316029910306332627414876684344367472209,
        "y": 89805716208030251512750858827899264938076397422929928838175186998853100491108
    }
}

slip10_nist256p1_private_key: IPrivateKey = SLIP10Nist256p1PrivateKey.from_bytes(data["private_key"])
ecc_slip10_nist256p1_private_key: IPrivateKey = ecc.PRIVATE_KEY.from_bytes(data["private_key"])

print(
    "Private Key:",
    ecc.NAME == slip10_nist256p1_private_key.name(),
    isinstance(slip10_nist256p1_private_key, SLIP10Nist256p1PrivateKey),
    isinstance(ecc_slip10_nist256p1_private_key, SLIP10Nist256p1PrivateKey),
    slip10_nist256p1_private_key.raw() == ecc_slip10_nist256p1_private_key.raw() == data["private_key"]
)

raw_slip10_nist256p1_point: IPoint = SLIP10Nist256p1Point.from_bytes(data["point"]["raw"])
coordinates_slip10_nist256p1_point: IPoint = SLIP10Nist256p1Point.from_coordinates(data["point"]["x"], data["point"]["y"])

print(
    "Point:",
    isinstance(raw_slip10_nist256p1_point, SLIP10Nist256p1Point),
    isinstance(coordinates_slip10_nist256p1_point, SLIP10Nist256p1Point),
    raw_slip10_nist256p1_point.raw() == coordinates_slip10_nist256p1_point.raw() ==
    ecc.POINT.from_bytes(data["point"]["raw"]).raw() ==
    ecc.POINT.from_coordinates(data["point"]["x"], data["point"]["y"]).raw() ==
    data["point"]["raw"]
)

slip10_nist256p1_public_key: IPublicKey = slip10_nist256p1_private_key.public_key()
ecc_slip10_nist256p1_public_key: IPublicKey = ecc_slip10_nist256p1_private_key.public_key()
uncompressed_public_key: IPublicKey = validate_and_get_public_key(data["public_key"]["uncompressed"], SLIP10Nist256p1PublicKey)
compressed_public_key: IPublicKey = validate_and_get_public_key(data["public_key"]["compressed"], SLIP10Nist256p1PublicKey)

print(
    "(Uncompressed) Public Key:",
    isinstance(slip10_nist256p1_public_key, SLIP10Nist256p1PublicKey),
    isinstance(ecc_slip10_nist256p1_public_key, SLIP10Nist256p1PublicKey),
    isinstance(uncompressed_public_key, SLIP10Nist256p1PublicKey),
    uncompressed_public_key.raw_uncompressed() == slip10_nist256p1_public_key.raw_uncompressed() ==
    ecc_slip10_nist256p1_public_key.raw_uncompressed() ==
    SLIP10Nist256p1PublicKey.from_bytes(data["public_key"]["uncompressed"]).raw_uncompressed() ==
    SLIP10Nist256p1PublicKey.from_point(raw_slip10_nist256p1_point).raw_uncompressed() ==
    ecc.PUBLIC_KEY.from_bytes(data["public_key"]["uncompressed"]).raw_uncompressed() ==
    ecc.PUBLIC_KEY.from_point(coordinates_slip10_nist256p1_point).raw_uncompressed() ==
    data["public_key"]["uncompressed"]
)

print(
    "(Compressed) Public Key:",
    isinstance(slip10_nist256p1_public_key, SLIP10Nist256p1PublicKey),
    isinstance(ecc_slip10_nist256p1_public_key, SLIP10Nist256p1PublicKey),
    isinstance(compressed_public_key, SLIP10Nist256p1PublicKey),
    compressed_public_key.raw_compressed() == slip10_nist256p1_public_key.raw_compressed() ==
    ecc_slip10_nist256p1_public_key.raw_compressed() ==
    SLIP10Nist256p1PublicKey.from_bytes(data["public_key"]["compressed"]).raw_compressed() ==
    SLIP10Nist256p1PublicKey.from_point(raw_slip10_nist256p1_point).raw_compressed() ==
    ecc.PUBLIC_KEY.from_bytes(data["public_key"]["compressed"]).raw_compressed() ==
    ecc.PUBLIC_KEY.from_point(coordinates_slip10_nist256p1_point).raw_compressed() ==
    data["public_key"]["compressed"]
)

print(
    "ECC:",
    SLIP10Nist256p1ECC.NAME == ecc.NAME ==
    slip10_nist256p1_private_key.name() == ecc_slip10_nist256p1_private_key.name() ==
    raw_slip10_nist256p1_point.name() == coordinates_slip10_nist256p1_point.name() ==
    slip10_nist256p1_public_key.name() == ecc_slip10_nist256p1_public_key.name() ==
    data["name"], "\n"
)

print("Elliptic Curve Cryptography:", data["name"])
print("Private Key:", bytes_to_string(data["private_key"]))
print("Point:", bytes_to_string(data["point"]["raw"]))
print("    x:", data["point"]["x"])
print("    y:", data["point"]["y"])
print("(Uncompressed) Public Key:", bytes_to_string(data["public_key"]["uncompressed"]))
print("(Compressed) Public Key:", bytes_to_string(data["public_key"]["compressed"]))
