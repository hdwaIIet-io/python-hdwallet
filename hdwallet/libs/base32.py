#!/usr/bin/env python3

from typing import Optional

import base64
import binascii


alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"


def add_padding(data: str) -> str:
    last_block_width = len(data) % 8
    if last_block_width != 0:
        data += (8 - last_block_width) * "="
    return data


def translate_alphabet(data: str, from_alphabet: str, to_alphabet: str) -> str:
    return data.translate(str.maketrans(from_alphabet, to_alphabet))


def decode(data: str, custom_alphabet: Optional[str] = None) -> str:
    try:
        data_decode = add_padding(data)
        if custom_alphabet:
            data_decode = translate_alphabet(data_decode, custom_alphabet, alphabet)

        return base64.b32decode(data_decode).hex()
    except binascii.Error as ex:
        raise ValueError("Invalid Base32 string") from ex


def encode(data: str, custom_alphabet: Optional[str] = None) -> str:
    b32_encode: str = base64.b32encode(binascii.unhexlify(data)).decode("utf-8")
    if custom_alphabet:
        b32_encode = translate_alphabet(b32_encode, alphabet, custom_alphabet)

    return b32_encode


def encode_no_padding(data: str, custom_alphabet: Optional[str] = None) -> str:
    return encode(data, custom_alphabet).rstrip("=")
