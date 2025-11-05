:orphan:

============================
Elliptic Curve Cryptographys
============================


.. autoclass:: hdwallet.eccs.ECCS
    :members:

.. autoclass:: hdwallet.eccs.iecc.IEllipticCurveCryptography
    :members:

.. autoclass:: hdwallet.eccs.kholaw.ed25519.KholawEd25519ECC
    :members:

.. autoclass:: hdwallet.eccs.kholaw.ed25519.point.KholawEd25519Point
    :members:

.. autoclass:: hdwallet.eccs.kholaw.ed25519.private_key.KholawEd25519PrivateKey
    :members:

>>> from hdwallet.eccs.kholaw.ed25519.private_key import KholawEd25519PrivateKey
>>> from hdwallet.utils import get_bytes
>>> KholawEd25519PrivateKey.name()
'Kholaw-Ed25519'
>>> KholawEd25519PrivateKey.length()
64
>>> private_key = KholawEd25519PrivateKey.from_bytes(
...     get_bytes("8061879a8fc9e7c685cb89b7014c85a6c4a2a8f3b6fa4964381d0751baf8fb5ff97530b002426a6eb1308e01372905d4c19c2b52a939bccd24c99a5826b9f87c")
... )
>>> private_key.raw().hex()
'8061879a8fc9e7c685cb89b7014c85a6c4a2a8f3b6fa4964381d0751baf8fb5ff97530b002426a6eb1308e01372905d4c19c2b52a939bccd24c99a5826b9f87c'
>>> private_key.public_key().raw_compressed().hex()
'00e55487c92c1913439f336b1b2dc316da6e88c02a157208f98781494b87f27eb8'
>>> private_key.public_key().raw_uncompressed().hex()
'00e55487c92c1913439f336b1b2dc316da6e88c02a157208f98781494b87f27eb8'


.. autoclass:: hdwallet.eccs.kholaw.ed25519.public_key.KholawEd25519PublicKey
    :members:

>>> from hdwallet.eccs.kholaw.ed25519 import KholawEd25519PublicKey
>>> from hdwallet.utils import get_bytes
>>> KholawEd25519PublicKey.name()
'Kholaw-Ed25519'
>>> public_key = KholawEd25519PublicKey.from_bytes(
...     get_bytes("00e55487c92c1913439f336b1b2dc316da6e88c02a157208f98781494b87f27eb8")
... )
>>> public_key.raw_compressed().hex()
'00e55487c92c1913439f336b1b2dc316da6e88c02a157208f98781494b87f27eb8'
>>> public_key.point().raw_encoded().hex()
'e55487c92c1913439f336b1b2dc316da6e88c02a157208f98781494b87f27eb8'
>>> public_key.point().x()
18529038270296824438026848489315401829943202020841826252456650783397010322849

.. autoclass:: hdwallet.eccs.slip10.ed25519.blake2b.SLIP10Ed25519Blake2bECC
    :members:

.. autoclass:: hdwallet.eccs.slip10.ed25519.blake2b.point.SLIP10Ed25519Blake2bPoint
    :members:

.. autoclass:: hdwallet.eccs.slip10.ed25519.blake2b.private_key.SLIP10Ed25519Blake2bPrivateKey
    :members:

>>> from hdwallet.eccs.slip10.ed25519.blake2b import SLIP10Ed25519Blake2bPrivateKey
>>> from hdwallet.utils import get_bytes
>>> SLIP10Ed25519Blake2bPrivateKey.name()
'SLIP10-Ed25519-Blake2b'
>>> SLIP10Ed25519Blake2bPrivateKey.length()
32
>>> private_key = SLIP10Ed25519Blake2bPrivateKey.from_bytes(
...     get_bytes("bb37794073e5094ebbfcfa070e9254fe6094b56e7cccb094a2304c5eccccdc07")
... )
>>> private_key.raw().hex()
'bb37794073e5094ebbfcfa070e9254fe6094b56e7cccb094a2304c5eccccdc07'
>>> private_key.public_key().raw_compressed().hex()
'006aea61eeed872052377ab16b0fc5d9b9f142be59ac1488e6610645dedb4da45c'
>>> private_key.public_key().raw_uncompressed().hex()
'006aea61eeed872052377ab16b0fc5d9b9f142be59ac1488e6610645dedb4da45c'


.. autoclass:: hdwallet.eccs.slip10.ed25519.blake2b.public_key.SLIP10Ed25519Blake2bPublicKey
    :members:

>>> from hdwallet.eccs.slip10.ed25519.blake2b import SLIP10Ed25519Blake2bPublicKey
>>> from hdwallet.utils import get_bytes
>>> SLIP10Ed25519Blake2bPublicKey.name()
'SLIP10-Ed25519-Blake2b'
>>> public_key = SLIP10Ed25519Blake2bPublicKey.from_bytes(
...     get_bytes("00d14696583ee9144878635b557d515a502b04366818dfe7765737746b4f57978d")
... )
>>> public_key.raw_compressed().hex()
'00d14696583ee9144878635b557d515a502b04366818dfe7765737746b4f57978d'
>>> public_key.point().raw_encoded().hex()
'd14696583ee9144878635b557d515a502b04366818dfe7765737746b4f57978d'
>>> public_key.point().x()
35008547582340824597639173221735807482318787407965447203743372716499096148063

.. autoclass:: hdwallet.eccs.slip10.ed25519.monero.SLIP10Ed25519MoneroECC
    :members:

.. autoclass:: hdwallet.eccs.slip10.ed25519.monero.point.SLIP10Ed25519MoneroPoint
    :members:

.. autoclass:: hdwallet.eccs.slip10.ed25519.monero.private_key.SLIP10Ed25519MoneroPrivateKey
    :members:

>>> from hdwallet.eccs.slip10.ed25519.monero import SLIP10Ed25519MoneroPrivateKey
>>> from hdwallet.utils import get_bytes
>>> SLIP10Ed25519MoneroPrivateKey.name()
'SLIP10-Ed25519-Monero'
>>> SLIP10Ed25519MoneroPrivateKey.length()
32
>>> private_key = SLIP10Ed25519MoneroPrivateKey.from_bytes(
...     get_bytes("bb37794073e5094ebbfcfa070e9254fe6094b56e7cccb094a2304c5eccccdc07")
... )
>>> private_key.raw().hex()
'bb37794073e5094ebbfcfa070e9254fe6094b56e7cccb094a2304c5eccccdc07'
>>> private_key.public_key().raw_compressed().hex()
'628247d3de93857cdd360fee4aef9a67ecfebedfe8eaec9cf6be35eacc895ca7'
>>> private_key.public_key().raw_uncompressed().hex()
'628247d3de93857cdd360fee4aef9a67ecfebedfe8eaec9cf6be35eacc895ca7'


.. autoclass:: hdwallet.eccs.slip10.ed25519.monero.public_key.SLIP10Ed25519MoneroPublicKey
    :members:

>>> from hdwallet.eccs.slip10.ed25519.monero import SLIP10Ed25519MoneroPublicKey
>>> from hdwallet.utils import get_bytes
>>> SLIP10Ed25519MoneroPublicKey.name()
'SLIP10-Ed25519-Monero'
>>> public_key = SLIP10Ed25519MoneroPublicKey.from_bytes(
...     get_bytes("628247d3de93857cdd360fee4aef9a67ecfebedfe8eaec9cf6be35eacc895ca7")
... )
>>> public_key.raw_compressed().hex()
'628247d3de93857cdd360fee4aef9a67ecfebedfe8eaec9cf6be35eacc895ca7'
>>> public_key.point().raw_encoded().hex()
'628247d3de93857cdd360fee4aef9a67ecfebedfe8eaec9cf6be35eacc895ca7'
>>> public_key.point().x()
29078407399097928298542937704975150613766572636435642857509307729044618011935

.. autoclass:: hdwallet.eccs.slip10.ed25519.SLIP10Ed25519ECC
    :members:

.. autoclass:: hdwallet.eccs.slip10.ed25519.point.SLIP10Ed25519Point
    :members:

.. autoclass:: hdwallet.eccs.slip10.ed25519.private_key.SLIP10Ed25519PrivateKey
    :members:

>>> from hdwallet.eccs.slip10.ed25519.private_key import SLIP10Ed25519PrivateKey
>>> from hdwallet.utils import get_bytes
>>> SLIP10Ed25519PrivateKey.name()
'SLIP10-Ed25519'
>>> SLIP10Ed25519PrivateKey.length()
32
>>> private_key = SLIP10Ed25519PrivateKey.from_bytes(
...     get_bytes("bb37794073e5094ebbfcfa070e9254fe6094b56e7cccb094a2304c5eccccdc07")
... )
>>> private_key.raw().hex()
'bb37794073e5094ebbfcfa070e9254fe6094b56e7cccb094a2304c5eccccdc07'
>>> private_key.public_key().raw_compressed().hex()
'00d14696583ee9144878635b557d515a502b04366818dfe7765737746b4f57978d'
>>> private_key.public_key().raw_uncompressed().hex()
'00d14696583ee9144878635b557d515a502b04366818dfe7765737746b4f57978d'

.. autoclass:: hdwallet.eccs.slip10.ed25519.public_key.SLIP10Ed25519PublicKey
    :members:

>>> from hdwallet.eccs.slip10.ed25519.public_key import SLIP10Ed25519PublicKey
>>> from hdwallet.utils import get_bytes
>>> SLIP10Ed25519PublicKey.name()
'SLIP10-Ed25519'
>>> public_key = SLIP10Ed25519PublicKey.from_bytes(
...     get_bytes("00d14696583ee9144878635b557d515a502b04366818dfe7765737746b4f57978d")
... )
>>> public_key.raw_compressed().hex()
'00d14696583ee9144878635b557d515a502b04366818dfe7765737746b4f57978d'
>>> public_key.point().raw_encoded().hex()
'd14696583ee9144878635b557d515a502b04366818dfe7765737746b4f57978d'
>>> public_key.point().x()
35008547582340824597639173221735807482318787407965447203743372716499096148063

.. autoclass:: hdwallet.eccs.slip10.nist256p1.SLIP10Nist256p1ECC
    :members:

.. autoclass:: hdwallet.eccs.slip10.nist256p1.point.SLIP10Nist256p1Point
    :members:

.. autoclass:: hdwallet.eccs.slip10.nist256p1.private_key.SLIP10Nist256p1PrivateKey
    :members:

>>> from hdwallet.eccs.slip10.nist256p1.private_key import SLIP10Nist256p1PrivateKey
>>> from hdwallet.utils import get_bytes
>>> SLIP10Nist256p1PrivateKey.name()
'SLIP10-Nist256p1'
>>> SLIP10Nist256p1PrivateKey.length()
32
>>> private_key = SLIP10Nist256p1PrivateKey.from_bytes(
...     get_bytes("f79495fda777197ce73551bcd8e162ceca19167575760d3cc2bced4bf2a213dc")
... )
>>> private_key.raw().hex()
'f79495fda777197ce73551bcd8e162ceca19167575760d3cc2bced4bf2a213dc'
>>> private_key.public_key().raw_compressed().hex()
'02e4bd97a82a8f3e575a9a35b7cca19cd730addd499a2bd4e9a9811df8bfc35e51'
>>> private_key.public_key().raw_uncompressed().hex()
'04e4bd97a82a8f3e575a9a35b7cca19cd730addd499a2bd4e9a9811df8bfc35e51c68c3bed41d47d4d05ae880250e4432cc6480b417597f1cffc5ed7d28991d164'

.. autoclass:: hdwallet.eccs.slip10.nist256p1.public_key.SLIP10Nist256p1PublicKey
    :members:

>>> from hdwallet.eccs.slip10.nist256p1.public_key import SLIP10Nist256p1PublicKey
>>> from hdwallet.utils import get_bytes
>>> SLIP10Nist256p1PublicKey.name()
'SLIP10-Nist256p1'
>>> public_key = SLIP10Nist256p1PublicKey.from_bytes(
...     get_bytes("02e4bd97a82a8f3e575a9a35b7cca19cd730addd499a2bd4e9a9811df8bfc35e51")
... )
>>> public_key.raw_compressed().hex()
'02e4bd97a82a8f3e575a9a35b7cca19cd730addd499a2bd4e9a9811df8bfc35e51'
>>> public_key.point().raw_encoded().hex()
'02e4bd97a82a8f3e575a9a35b7cca19cd730addd499a2bd4e9a9811df8bfc35e51'
>>> public_key.point().x()
103462310269679299860340333843259692621316029910306332627414876684344367472209

.. autoclass:: hdwallet.eccs.slip10.secp256k1.SLIP10Secp256k1ECC
    :members:

.. autoclass:: hdwallet.eccs.slip10.secp256k1.SLIP10Secp256k1ECCCoincurve
    :members:

.. autoclass:: hdwallet.eccs.slip10.secp256k1.point.SLIP10Secp256k1PointCoincurve
    :members:

.. autoclass:: hdwallet.eccs.slip10.secp256k1.private_key.SLIP10Secp256k1PrivateKeyCoincurve
    :members:

>>> from hdwallet.eccs.slip10.secp256k1.private_key import SLIP10Secp256k1PrivateKeyCoincurve
>>> from hdwallet.utils import get_bytes
>>> SLIP10Secp256k1PrivateKeyCoincurve.name()
'SLIP10-Secp256k1'
>>> SLIP10Secp256k1PrivateKeyCoincurve.length()
32
>>> private_key = SLIP10Secp256k1PrivateKeyCoincurve.from_bytes(
...     get_bytes("b66022fff8b6322f8b8fa444d6d097457b6b9e7bb05add5b75f9c827df7bd3b6")
... )
>>> private_key.raw().hex()
'b66022fff8b6322f8b8fa444d6d097457b6b9e7bb05add5b75f9c827df7bd3b6'
>>> private_key.public_key().raw_compressed().hex()
'0374a436044b4904bbd7a074b098d65fad39fc5b66f28da8440f10dbcf86568429'
>>> private_key.public_key().raw_uncompressed().hex()
'0474a436044b4904bbd7a074b098d65fad39fc5b66f28da8440f10dbcf86568429aae5b09b4de9cee5d2f9f98044f688aa98f910134a8e87eff28ec5ba35ddf273'

.. autoclass:: hdwallet.eccs.slip10.secp256k1.public_key.SLIP10Secp256k1PublicKeyCoincurve
    :members:

>>> from hdwallet.eccs.slip10.secp256k1.public_key import SLIP10Secp256k1PublicKeyCoincurve
>>> from hdwallet.utils import get_bytes
>>> SLIP10Secp256k1PublicKeyCoincurve.name()
'SLIP10-Secp256k1'
>>> public_key = SLIP10Secp256k1PublicKeyCoincurve.from_bytes(
...     get_bytes("0374a436044b4904bbd7a074b098d65fad39fc5b66f28da8440f10dbcf86568429")
... )
>>> public_key.raw_compressed().hex()
'0374a436044b4904bbd7a074b098d65fad39fc5b66f28da8440f10dbcf86568429'
>>> public_key.point().raw_encoded().hex()
'0374a436044b4904bbd7a074b098d65fad39fc5b66f28da8440f10dbcf86568429'
>>> public_key.point().x()
52758426164353529380574599868388529660378638078403259786555024244882051335209

.. autoclass:: hdwallet.eccs.slip10.secp256k1.SLIP10Secp256k1ECCECDSA
    :members:

.. autoclass:: hdwallet.eccs.slip10.secp256k1.point.SLIP10Secp256k1PointECDSA
    :members:

.. autoclass:: hdwallet.eccs.slip10.secp256k1.private_key.SLIP10Secp256k1PrivateKeyECDSA
    :members:

>>> from hdwallet.eccs.slip10.secp256k1.private_key import SLIP10Secp256k1PrivateKeyECDSA
>>> from hdwallet.utils import get_bytes
>>> SLIP10Secp256k1PrivateKeyECDSA.name()
'SLIP10-Secp256k1'
>>> SLIP10Secp256k1PrivateKeyECDSA.length()
32
>>> private_key = SLIP10Secp256k1PrivateKeyECDSA.from_bytes(
...     get_bytes("b66022fff8b6322f8b8fa444d6d097457b6b9e7bb05add5b75f9c827df7bd3b6")
... )
>>> private_key.raw().hex()
'b66022fff8b6322f8b8fa444d6d097457b6b9e7bb05add5b75f9c827df7bd3b6'
>>> private_key.public_key().raw_compressed().hex()
'0374a436044b4904bbd7a074b098d65fad39fc5b66f28da8440f10dbcf86568429'
>>> private_key.public_key().raw_uncompressed().hex()
'0474a436044b4904bbd7a074b098d65fad39fc5b66f28da8440f10dbcf86568429aae5b09b4de9cee5d2f9f98044f688aa98f910134a8e87eff28ec5ba35ddf273'

.. autoclass:: hdwallet.eccs.slip10.secp256k1.public_key.SLIP10Secp256k1PublicKeyECDSA
    :members:

>>> from hdwallet.eccs.slip10.secp256k1.public_key import SLIP10Secp256k1PublicKeyECDSA
>>> from hdwallet.utils import get_bytes
>>> SLIP10Secp256k1PublicKeyECDSA.name()
'SLIP10-Secp256k1'
>>> public_key = SLIP10Secp256k1PublicKeyECDSA.from_bytes(
...     get_bytes("0374a436044b4904bbd7a074b098d65fad39fc5b66f28da8440f10dbcf86568429")
... )
>>> public_key.raw_compressed().hex()
'0374a436044b4904bbd7a074b098d65fad39fc5b66f28da8440f10dbcf86568429'
>>> public_key.point().raw_encoded().hex()
'0374a436044b4904bbd7a074b098d65fad39fc5b66f28da8440f10dbcf86568429'
>>> public_key.point().x()
52758426164353529380574599868388529660378638078403259786555024244882051335209
