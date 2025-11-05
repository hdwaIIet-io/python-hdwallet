#!/usr/bin/env python3

# Copyright © 2020-2025, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from .ipoint import IPoint
from .ipublic_key import IPublicKey
from .iprivate_key import IPrivateKey


class IEllipticCurveCryptography:
    """
    Interface for Elliptic Curve Cryptography (ECC) representation.

    This interface defines the key components and attributes required
    for elliptic curve cryptography operations. It is intended to be
    implemented by specific ECC classes.
    """

    NAME: str
    ORDER: int
    GENERATOR: IPoint
    POINT: IPoint
    PUBLIC_KEY: IPublicKey
    PRIVATE_KEY: IPrivateKey
