#!/usr/bin/env python3

from hdwallet.eccs import (
    IPrivateKey, IPublicKey, KholawEd25519PrivateKey
)
from hdwallet.addresses.cardano import CardanoAddress
from hdwallet.cryptocurrencies import Cardano
from hdwallet.utils import (
    bytes_to_string, get_bytes
)

private_key: IPrivateKey = KholawEd25519PrivateKey.from_bytes(get_bytes(
    "8061879a8fc9e7c685cb89b7014c85a6c4a2a8f3b6fa4964381d0751baf8fb5ff97530b002426a6eb1308e01372905d4c19c2b52a939bccd24c99a5826b9f87c"
))
public_key: IPublicKey = private_key.public_key()

print("Private Key:", bytes_to_string(private_key.raw()))
print("Uncompressed Public Key:", bytes_to_string(public_key.raw_uncompressed()))
print("Compressed Public Key:", bytes_to_string(public_key.raw_compressed()), "\n")

byron_icarus_address: str = CardanoAddress.encode(
    public_key=public_key.raw_compressed(),
    encode_type=Cardano.TYPES.BYRON_ICARUS,
    chain_code="d537f39c41f0f781f543c4c512cac38927e5ebd3cd82b870dd7ce94de9e510b4"
)
byron_icarus_address_hash: str = CardanoAddress.decode(
    address=byron_icarus_address, decode_type=Cardano.TYPES.BYRON_ICARUS
)
print("Byron-Icarus Address:", byron_icarus_address, byron_icarus_address_hash)

byron_legacy_address: str = CardanoAddress.encode(
    public_key=public_key.raw_compressed(),
    encode_type=Cardano.TYPES.BYRON_LEGACY,
    path="m/0'/0234'/123/243/5/7",
    path_key="39ddaa1e5719d88d6b53eda320f3dbe8c012d24abe33f4ac358fe78df43d5814",
    chain_code="d537f39c41f0f781f543c4c512cac38927e5ebd3cd82b870dd7ce94de9e510b4"
)
byron_legacy_address_hash: str = CardanoAddress.decode(
    address=byron_legacy_address, decode_type=Cardano.TYPES.BYRON_LEGACY
)
print("Byron-Legacy Address:", byron_legacy_address, byron_legacy_address_hash)

shelley_address: str = CardanoAddress.encode(
    public_key=public_key.raw_compressed(),
    encode_type=Cardano.ADDRESS_TYPES.PAYMENT,
    staking_public_key="007505bd415a4d5b21cb5be55360adeff02192ad952b5a1728e65010aea306aa54",
    network="mainnet"
)
shelley_address_hash: str = CardanoAddress.decode(
    address=shelley_address,
    decode_type=Cardano.ADDRESS_TYPES.PAYMENT,
    network="mainnet"
)
print("Shelley Address:",  shelley_address, shelley_address_hash)

shelley_staking_address: str = CardanoAddress.encode(
    public_key=public_key.raw_compressed(),
    encode_type=Cardano.ADDRESS_TYPES.STAKING,
    network="mainnet"
)
shelley_staking_address_hash: str = CardanoAddress.decode(
    address=shelley_staking_address,
    decode_type=Cardano.ADDRESS_TYPES.STAKING,
    network="mainnet"
)
print("Cardano Shelley Staking Address:",  shelley_staking_address, shelley_staking_address_hash)
