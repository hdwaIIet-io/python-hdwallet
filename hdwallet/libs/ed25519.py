#!/usr/bin/env python3

from typing import (
    Tuple, Union, Optional, Literal
)
from binascii import unhexlify
from nacl.bindings import (
    crypto_core_ed25519_add,
    crypto_scalarmult_ed25519_noclamp,
    crypto_scalarmult_ed25519_base_noclamp,
    crypto_core_ed25519_scalar_reduce
)

_Q = 2 ** 255 - 19
_L = 2 ** 252 + 27742317777372353535851937790883648493
_G = (
    15112221349535400772501151409588531511454012693041857206046113283949847762202,
    46316835694926478169428394003475163141307993866256225615783033603165251855960
)
_G_DEC_BYTES = unhexlify(
    "1ad5258f602d56c9b2a7259560c72c695cdcd6fd31e2a4c0fe536ecdd3366921"
    "5866666666666666666666666666666666666666666666666666666666666666"
)
_G_ENC_BYTES = unhexlify(
    "5866666666666666666666666666666666666666666666666666666666666666"
)
_COORD_BYTE_LEN = 32


def bytes_to_integer(data: bytes, endianness: Literal["little", "big"] = "big", signed: bool = False) -> int:
    return int.from_bytes(data, byteorder=endianness, signed=signed)


def integer_to_bytes(data: int, bytes_num: Optional[int] = None, endianness: Literal["little", "big"] = "big", signed: bool = False) -> bytes:
    bytes_num = bytes_num or ((data.bit_length() if data > 0 else 1) + 7) // 8
    return data.to_bytes(bytes_num, byteorder=endianness, signed=signed)


def _inv(x: int) -> int:
    return pow(x, _Q - 2, _Q)


_D = -121665 * _inv(121666)
_I = pow(2, (_Q - 1) // 4, _Q)  # noqa: E741


def _x_recover(y: int) -> int:
    xx = (y * y - 1) * _inv(_D * y * y + 1)
    x = pow(xx, (_Q + 3) // 8, _Q)
    if (x * x - xx) % _Q != 0:
        x = (x * _I) % _Q
    if x % 2 != 0:
        x = _Q - x
    return x


def int_decode(int_bytes: bytes) -> int:
    return bytes_to_integer(int_bytes, endianness="little")


def int_encode(int_val: int) -> bytes:
    return integer_to_bytes(int_val, _COORD_BYTE_LEN, endianness="little")


def point_is_decoded_bytes(point_bytes: bytes) -> bool:
    return len(point_bytes) == _COORD_BYTE_LEN * 2


def point_is_encoded_bytes(point_bytes: bytes) -> bool:
    return len(point_bytes) == _COORD_BYTE_LEN


def point_is_valid_bytes(point_bytes: bytes) -> bool:
    return point_is_decoded_bytes(point_bytes) or point_is_encoded_bytes(point_bytes)


def point_bytes_to_coord(point_bytes: bytes) -> Tuple[int, int]:
    if point_is_decoded_bytes(point_bytes):
        return int_decode(point_bytes[:_COORD_BYTE_LEN]), int_decode(point_bytes[_COORD_BYTE_LEN:])
    if point_is_encoded_bytes(point_bytes):
        return point_decode_no_check(point_bytes)
    raise ValueError("Invalid point bytes")


def point_coord_to_bytes(point_coord: Tuple[int, int]) -> bytes:
    return int_encode(point_coord[0]) + int_encode(point_coord[1])


def point_decode_no_check(point_bytes: bytes) -> Tuple[int, int]:
    if not point_is_encoded_bytes(point_bytes):
        raise ValueError("Invalid point bytes")

    point_int = int_decode(point_bytes)

    clamp = (1 << 255) - 1
    y = point_int & clamp
    x = _x_recover(y)
    if bool(x & 1) != bool(point_int & (1 << 255)):
        x = _Q - x

    return x, y


def point_decode(point_bytes: bytes) -> Tuple[int, int]:
    point_coord = point_decode_no_check(point_bytes)
    if not point_is_on_curve(point_coord):
        raise ValueError("Decoded point does not lie on the curve")
    return point_coord


def point_encode(point_coord: Tuple[int, int]) -> bytes:
    point_bytes = point_coord_to_bytes(point_coord)

    y_bytes = bytearray(point_bytes[_COORD_BYTE_LEN:])
    if point_bytes[0] & 1:
        y_bytes[len(y_bytes) - 1] |= 0x80
    return bytes(y_bytes)


def point_is_generator(point: Union[bytes, Tuple[int, int]]) -> bool:
    # Avoid converting to coordinates if bytes to increase speed
    if isinstance(point, bytes):
        if point_is_encoded_bytes(point):
            return point == _G_ENC_BYTES
        if point_is_decoded_bytes(point):
            return point == _G_DEC_BYTES
        raise ValueError("Invalid point bytes")
    return point == _G


def point_is_on_curve(point: Union[bytes, Tuple[int, int]]) -> bool:
    if isinstance(point, bytes):
        point = point_bytes_to_coord(point)

    x = point[0]
    y = point[1]
    return (-x * x + y * y - 1 - _D * x * x * y * y) % _Q == 0


def point_add(point_1: Union[bytes, Tuple[int, int]],
              point_2: Union[bytes, Tuple[int, int]]) -> bytes:
    return crypto_core_ed25519_add(
        point_1 if isinstance(point_1, bytes) else point_encode(point_1),
        point_2 if isinstance(point_2, bytes) else point_encode(point_2)
    )


def point_scalar_mul(scalar: Union[bytes, int],
                     point: Union[bytes, Tuple[int, int]]) -> bytes:
    return crypto_scalarmult_ed25519_noclamp(
        scalar if isinstance(scalar, bytes) else int_encode(scalar),
        point if isinstance(point, bytes) else point_encode(point)
    )


def point_scalar_mul_base(scalar: Union[bytes, int]) -> bytes:
    return crypto_scalarmult_ed25519_base_noclamp(
        scalar if isinstance(scalar, bytes) else int_encode(scalar)
    )


def scalar_reduce(scalar: Union[bytes, int]) -> bytes:
    if isinstance(scalar, int):
        scalar = int_encode(scalar)
    return crypto_core_ed25519_scalar_reduce(
        scalar.ljust(_COORD_BYTE_LEN * 2, b"\x00")
    )


def scalar_is_valid(scalar: Union[bytes, int]) -> bool:
    if isinstance(scalar, bytes):
        scalar = int_decode(scalar)
    return scalar < _L
