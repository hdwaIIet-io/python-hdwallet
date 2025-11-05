#!/usr/bin/env python3

from typing import Type

from hdwallet.eccs import (
    IEllipticCurveCryptography,
    IPrivateKey,
    IPublicKey,
    IPoint,
    ECCS,
    validate_and_get_public_key,
    KholawEd25519ECC,
    KholawEd25519Point,
    KholawEd25519PublicKey,
    KholawEd25519PrivateKey,
)
from hdwallet.utils import get_bytes, bytes_to_string

ecc: Type[IEllipticCurveCryptography] = ECCS.ecc(KholawEd25519ECC.NAME)

data = {
    "name": "Kholaw-Ed25519",
    "private_key": get_bytes("8061879a8fc9e7c685cb89b7014c85a6c4a2a8f3b6fa4964381d0751baf8fb5ff97530b002426a6eb1308e01372905d4c19c2b52a939bccd24c99a5826b9f87c"),
    "public_key": {
        "uncompressed": get_bytes("00e55487c92c1913439f336b1b2dc316da6e88c02a157208f98781494b87f27eb8"),
        "compressed": get_bytes("00e55487c92c1913439f336b1b2dc316da6e88c02a157208f98781494b87f27eb8")
    },
    "point": {
        "raw": get_bytes("e55487c92c1913439f336b1b2dc316da6e88c02a157208f98781494b87f27eb8"),
        "x": 18529038270296824438026848489315401829943202020841826252456650783397010322849,
        "y": 25553816120962378038042195812249947304098260420554035661068256958789815063781
    }
}

kholaw_ed25519_private_key: IPrivateKey = KholawEd25519PrivateKey.from_bytes(data["private_key"])
ecc_kholaw_ed25519_private_key: IPrivateKey = ecc.PRIVATE_KEY.from_bytes(data["private_key"])

print(
    "Private Key:",
    ecc.NAME == kholaw_ed25519_private_key.name(),
    isinstance(kholaw_ed25519_private_key, KholawEd25519PrivateKey),
    isinstance(ecc_kholaw_ed25519_private_key, KholawEd25519PrivateKey),
    kholaw_ed25519_private_key.raw() == ecc_kholaw_ed25519_private_key.raw() == data["private_key"]
)

raw_kholaw_ed25519_point: IPoint = KholawEd25519Point.from_bytes(data["point"]["raw"])
coordinates_kholaw_ed25519_point: IPoint = KholawEd25519Point.from_coordinates(data["point"]["x"], data["point"]["y"])

print(
    "Point:",
    isinstance(raw_kholaw_ed25519_point, KholawEd25519Point),
    isinstance(coordinates_kholaw_ed25519_point, KholawEd25519Point),
    raw_kholaw_ed25519_point.raw() == coordinates_kholaw_ed25519_point.raw() ==
    ecc.POINT.from_bytes(data["point"]["raw"]).raw() ==
    ecc.POINT.from_coordinates(data["point"]["x"], data["point"]["y"]).raw() ==
    data["point"]["raw"]
)

kholaw_ed25519_public_key: IPublicKey = kholaw_ed25519_private_key.public_key()
ecc_kholaw_ed25519_public_key: IPublicKey = ecc_kholaw_ed25519_private_key.public_key()
uncompressed_public_key: IPublicKey = validate_and_get_public_key(data["public_key"]["uncompressed"], KholawEd25519PublicKey)
compressed_public_key: IPublicKey = validate_and_get_public_key(data["public_key"]["compressed"], KholawEd25519PublicKey)

print(
    "(Uncompressed) Public Key:",
    isinstance(kholaw_ed25519_public_key, KholawEd25519PublicKey),
    isinstance(ecc_kholaw_ed25519_public_key, KholawEd25519PublicKey),
    isinstance(uncompressed_public_key, KholawEd25519PublicKey),
    uncompressed_public_key.raw_uncompressed() == kholaw_ed25519_public_key.raw_uncompressed() ==
    ecc_kholaw_ed25519_public_key.raw_uncompressed() ==
    KholawEd25519PublicKey.from_bytes(data["public_key"]["uncompressed"]).raw_uncompressed() ==
    KholawEd25519PublicKey.from_point(raw_kholaw_ed25519_point).raw_uncompressed() ==
    ecc.PUBLIC_KEY.from_bytes(data["public_key"]["uncompressed"]).raw_uncompressed() ==
    ecc.PUBLIC_KEY.from_point(coordinates_kholaw_ed25519_point).raw_uncompressed() ==
    data["public_key"]["uncompressed"]
)

print(
    "(Compressed) Public Key:",
    isinstance(kholaw_ed25519_public_key, KholawEd25519PublicKey),
    isinstance(ecc_kholaw_ed25519_public_key, KholawEd25519PublicKey),
    isinstance(compressed_public_key, KholawEd25519PublicKey),
    compressed_public_key.raw_compressed() == kholaw_ed25519_public_key.raw_compressed() ==
    ecc_kholaw_ed25519_public_key.raw_compressed() ==
    KholawEd25519PublicKey.from_bytes(data["public_key"]["compressed"]).raw_compressed() ==
    KholawEd25519PublicKey.from_point(raw_kholaw_ed25519_point).raw_compressed() ==
    ecc.PUBLIC_KEY.from_bytes(data["public_key"]["compressed"]).raw_compressed() ==
    ecc.PUBLIC_KEY.from_point(coordinates_kholaw_ed25519_point).raw_compressed() ==
    data["public_key"]["compressed"]
)

print(
    "ECC:",
    KholawEd25519ECC.NAME == ecc.NAME ==
    kholaw_ed25519_private_key.name() == ecc_kholaw_ed25519_private_key.name() ==
    raw_kholaw_ed25519_point.name() == coordinates_kholaw_ed25519_point.name() ==
    kholaw_ed25519_public_key.name() == ecc_kholaw_ed25519_public_key.name() ==
    data["name"], "\n"
)

print("Elliptic Curve Cryptography:", data["name"])
print("Private Key:", bytes_to_string(data["private_key"]))
print("Point:", bytes_to_string(data["point"]["raw"]))
print("    x:", data["point"]["x"])
print("    y:", data["point"]["y"])
print("(Uncompressed) Public Key:", bytes_to_string(data["public_key"]["uncompressed"]))
print("(Compressed) Public Key:", bytes_to_string(data["public_key"]["compressed"]))
