:orphan:

============================
Hierarchical Deterministic's
============================

.. autoclass:: hdwallet.hds.HDS
    :members:

>>> from hdwallet.hds import HDS
>>> HDS.names()
['Algorand', 'BIP32', 'BIP44', 'BIP49', 'BIP84', 'BIP86', 'BIP141', 'Cardano', 'Electrum-V1', 'Electrum-V2', 'Monero']
>>> HDS.classes()
[<class 'hdwallet.hds.algorand.AlgorandHD'>, <class 'hdwallet.hds.bip32.BIP32HD'>, <class 'hdwallet.hds.bip44.BIP44HD'>, <class 'hdwallet.hds.bip49.BIP49HD'>, <class 'hdwallet.hds.bip84.BIP84HD'>, <class 'hdwallet.hds.bip86.BIP86HD'>, <class 'hdwallet.hds.bip141.BIP141HD'>, <class 'hdwallet.hds.cardano.CardanoHD'>, <class 'hdwallet.hds.electrum.v1.ElectrumV1HD'>, <class 'hdwallet.hds.electrum.v2.ElectrumV2HD'>, <class 'hdwallet.hds.monero.MoneroHD'>]
>>> from hdwallet.hds.electrum.v2 import ElectrumV2HD
>>> HDS.hd(name="BIP32")
<class 'hdwallet.hds.bip32.BIP32HD'>
>>> HDS.hd(name="Electrum-V2") == ElectrumV2HD
True
>>> HDS.is_hd(name="Electrum-V1")
True

.. autoclass:: hdwallet.hds.ihd.IHD
    :members:

.. autoclass:: hdwallet.hds.algorand.AlgorandHD
    :members:

Example: https://github.com/hdwallet-io/python-hdwallet/blob/master/examples/hds/algorand.py

.. autoclass:: hdwallet.hds.bip32.BIP32HD
    :members:

Example: https://github.com/hdwallet-io/python-hdwallet/blob/master/examples/hds/bip32.py

.. autoclass:: hdwallet.hds.bip44.BIP44HD
    :members:

Example: https://github.com/hdwallet-io/python-hdwallet/blob/master/examples/hds/bip44.py

.. autoclass:: hdwallet.hds.bip49.BIP49HD
    :members:

Example: https://github.com/hdwallet-io/python-hdwallet/blob/master/examples/hds/bip49.py

.. autoclass:: hdwallet.hds.bip84.BIP84HD
    :members:

Example: https://github.com/hdwallet-io/python-hdwallet/blob/master/examples/hds/bip84.py

.. autoclass:: hdwallet.hds.bip86.BIP86HD
    :members:

Example: https://github.com/hdwallet-io/python-hdwallet/blob/master/examples/hds/bip86.py

.. autoclass:: hdwallet.hds.bip141.BIP141HD
    :members:

Example: https://github.com/hdwallet-io/python-hdwallet/blob/master/examples/hds/bip141.py

.. autoclass:: hdwallet.hds.cardano.CardanoHD
    :members:

Example: https://github.com/hdwallet-io/python-hdwallet/tree/master/examples/hds/cardano

.. autoclass:: hdwallet.hds.electrum.v1.ElectrumV1HD
    :members:

Example: https://github.com/hdwallet-io/python-hdwallet/blob/master/examples/hds/electrum/v1.py

.. autoclass:: hdwallet.hds.electrum.v2.ElectrumV2HD
    :members:

Example: https://github.com/hdwallet-io/python-hdwallet/tree/master/examples/hds/electrum/v2

.. autoclass:: hdwallet.hds.monero.MoneroHD
    :members:

Example: https://github.com/hdwallet-io/python-hdwallet/blob/master/examples/hds/monero.py
