:orphan:

=========
Entropies
=========

.. autoclass:: hdwallet.entropies.ENTROPIES
    :members:

>>> from hdwallet.entropies import ENTROPIES
>>> ENTROPIES.names()
['Algorand', 'BIP39', 'Electrum-V1', 'Electrum-V2', 'Monero']
>>> ENTROPIES.classes()
[<class 'hdwallet.entropies.algorand.AlgorandEntropy'>, <class 'hdwallet.entropies.bip39.BIP39Entropy'>, <class 'hdwallet.entropies.electrum.v1.ElectrumV1Entropy'>, <class 'hdwallet.entropies.electrum.v2.ElectrumV2Entropy'>, <class 'hdwallet.entropies.monero.MoneroEntropy'>]
>>> from hdwallet.entropies import BIP39Entropy
>>> ENTROPIES.entropy(name="BIP39")
<class 'hdwallet.entropies.bip39.BIP39Entropy'>
>>> ENTROPIES.entropy(name="BIP39") == BIP39Entropy
True
>>> ENTROPIES.is_entropy(name="Electrum-V2")
True

.. autoclass:: hdwallet.entropies.ientropy.IEntropy
    :members:

.. autoclass:: hdwallet.entropies.algorand.AlgorandEntropy
    :members:

>>> from hdwallet.entropies.algorand import AlgorandEntropy, ALGORAND_ENTROPY_STRENGTHS
>>> entropy: str = AlgorandEntropy.generate(
...     strength=ALGORAND_ENTROPY_STRENGTHS.TWO_HUNDRED_FIFTY_SIX
... )
>>> entropy
'5e4d59d4c056b9f0dc9871e8f30194a6b67de1742df9a3f23dc4b9ee8f73b51e'
>>> algorand_entropy: AlgorandEntropy = AlgorandEntropy(entropy=entropy)
>>> algorand_entropy.name()
'Algorand'
>>> algorand_entropy.entropy()
'5e4d59d4c056b9f0dc9871e8f30194a6b67de1742df9a3f23dc4b9ee8f73b51e'
>>> algorand_entropy.strength()
256

.. autoclass:: hdwallet.entropies.bip39.BIP39Entropy
    :members:

>>> from hdwallet.entropies.bip39 import BIP39Entropy, BIP39_ENTROPY_STRENGTHS
>>> entropy: str = BIP39Entropy.generate(
    strength=BIP39_ENTROPY_STRENGTHS.ONE_HUNDRED_TWENTY_EIGHT
)
>>> entropy
"89f89c8d5445f37dde5d70212bf3f6b4"
>>> bip39_entropy: BIP39Entropy = BIP39Entropy(entropy=entropy)
>>> bip39_entropy.name()
"BIP39"
>>> bip39_entropy.entropy()
"89f89c8d5445f37dde5d70212bf3f6b4"
>>> bip39_entropy.strength()
128

.. autoclass:: hdwallet.entropies.electrum.v1.ElectrumV1Entropy
    :members:

>>> from hdwallet.entropies.electrum.v1 import ElectrumV1Entropy, ELECTRUM_V1_ENTROPY_STRENGTHS
>>> entropy: str = ElectrumV1Entropy.generate(
...     strength=ELECTRUM_V1_ENTROPY_STRENGTHS.ONE_HUNDRED_TWENTY_EIGHT
... )
>>> entropy
'9b96654fbbd35cb4d4e7c6c118cf6a5e'
>>> ev1_entropy: ElectrumV1Entropy = ElectrumV1Entropy(entropy=entropy)
>>> ev1_entropy.name()
'Electrum-V1'
>>> ev1_entropy.entropy()
'9b96654fbbd35cb4d4e7c6c118cf6a5e'
>>> ev1_entropy.strength()
128

.. autoclass:: hdwallet.entropies.electrum.v2.ElectrumV2Entropy
    :members:

>>> from hdwallet.entropies.electrum.v2 import ElectrumV2Entropy, ELECTRUM_V2_ENTROPY_STRENGTHS
>>> entropy: str = ElectrumV2Entropy.generate(
...     strength=ELECTRUM_V2_ENTROPY_STRENGTHS.TWO_HUNDRED_SIXTY_FOUR
... )
>>> entropy
'997cf5c9ab01f11e0d61a43a8abdb4740903043f7c1befbba1e356212c82fcac4f'
>>> ev2_entropy: ElectrumV2Entropy = ElectrumV2Entropy(entropy=entropy)
>>> ev2_entropy.name()
'Electrum-V2'
>>> ev2_entropy.entropy()
'997cf5c9ab01f11e0d61a43a8abdb4740903043f7c1befbba1e356212c82fcac4f'
>>> ev2_entropy.strength()
264
>>> ElectrumV2Entropy.generate(strength=ELECTRUM_V2_ENTROPY_STRENGTHS.TWO_HUNDRED_SIXTY_FOUR)
'c7902e83f0343317faa44df15df60688d2c5a1ca5c496c3efb77d4650ccc834383'
>>> ElectrumV2Entropy.is_valid_strength(strength=ELECTRUM_V2_ENTROPY_STRENGTHS.TWO_HUNDRED_SIXTY_FOUR)
True

.. autoclass:: hdwallet.entropies.monero.MoneroEntropy
    :members:

>>> from hdwallet.entropies.monero import MoneroEntropy, MONERO_ENTROPY_STRENGTHS
>>> entropy: str = MoneroEntropy.generate(
...     strength=MONERO_ENTROPY_STRENGTHS.TWO_HUNDRED_FIFTY_SIX
... )
>>> entropy
'9718cfa416a1c6dfc7126759b88c545130b8fe36f30e0365d9e48f1bf3ca906e'
>>> monero_entropy: MoneroEntropy = MoneroEntropy(entropy=entropy)
>>> monero_entropy.name()
'Monero'
>>> monero_entropy.entropy()
'9718cfa416a1c6dfc7126759b88c545130b8fe36f30e0365d9e48f1bf3ca906e'
>>> monero_entropy.strength()
256
