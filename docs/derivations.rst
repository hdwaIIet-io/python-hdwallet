===========
Derivations
===========

.. autoclass:: hdwallet.derivations.DERIVATIONS
    :members:

>>> from hdwallet.derivations import DERIVATIONS
>>> DERIVATIONS.names()
['BIP44', 'BIP49', 'BIP84', 'BIP86', 'CIP1852', 'Custom', 'Electrum', 'Monero']
>>> DERIVATIONS.classes()
[<class 'hdwallet.derivations.bip44.BIP44Derivation'>, <class 'hdwallet.derivations.bip49.BIP49Derivation'>, <class 'hdwallet.derivations.bip84.BIP84Derivation'>, <class 'hdwallet.derivations.bip86.BIP86Derivation'>, <class 'hdwallet.derivations.cip1852.CIP1852Derivation'>, <class 'hdwallet.derivations.custom.CustomDerivation'>, <class 'hdwallet.derivations.electrum.ElectrumDerivation'>, <class 'hdwallet.derivations.monero.MoneroDerivation'>]
>>> DERIVATIONS.derivation(name="BIP44")
<class 'hdwallet.derivations.bip44.BIP44Derivation'>
>>> DERIVATIONS.is_derivation(name="BIP44")
True

.. autoclass:: hdwallet.derivations.iderivation.IDerivation
    :members:

.. autoclass:: hdwallet.derivations.bip44.BIP44Derivation
    :members:

>>> from hdwallet.derivations.bip44 import BIP44Derivation, CHANGES
>>> BIP44Derivation.name()
'BIP44'
>>> bip44_derivation: BIP44Derivation = BIP44Derivation()
>>> bip44_derivation.path()
"m/44'/0'/0'/0/0"
>>> bip44_derivation.from_coin_type(coin_type=11)
<hdwallet.derivations.bip44.BIP44Derivation object at 0x000001EF69834D00>
>>> bip44_derivation.from_account(account=1)
<hdwallet.derivations.bip44.BIP44Derivation object at 0x000001EF69834D00>
>>> bip44_derivation.from_change(change="external-chain")
<hdwallet.derivations.bip44.BIP44Derivation object at 0x000001EF69834D00>
>>> bip44_derivation.from_address(address=10)
<hdwallet.derivations.bip44.BIP44Derivation object at 0x000001EF69834D00>
>>> bip44_derivation.from_coin_type(coin_type=11)
<hdwallet.derivations.bip44.BIP44Derivation object at 0x000001EF69834D00>
>>> bip44_derivation.path()
"m/44'/11'/1'/0/10"
>>> bip44_derivation.indexes()
[2147483692, 2147483659, 2147483649, 0, 10]
>>> bip44_derivation: BIP44Derivation = BIP44Derivation(coin_type=11, account=1, change=CHANGES.EXTERNAL_CHAIN, address=10)
>>> bip44_derivation.purpose()
44
>>> bip44_derivation.coin_type()
11
>>> bip44_derivation.account()
1
>>> bip44_derivation.change()
'external-chain'
>>> bip44_derivation.address()
10

.. autoclass:: hdwallet.derivations.bip49.BIP49Derivation
    :members:

>>> from hdwallet.derivations import CHANGES
>>> from hdwallet.derivations.bip49 import BIP49Derivation
>>> BIP49Derivation.name()
'BIP49'
>>> bip49_derivation: BIP49Derivation = BIP49Derivation()
>>> bip49_derivation.path()
"m/49'/0'/0'/0/0"
>>> bip49_derivation.from_coin_type(coin_type=11)
<hdwallet.derivations.bip49.BIP49Derivation object at 0x000001A0CC9F75B0>
>>> bip49_derivation.from_account(account=1)
<hdwallet.derivations.bip49.BIP49Derivation object at 0x000001A0CC9F75B0>
>>> bip49_derivation.from_change(change="external-chain")
<hdwallet.derivations.bip49.BIP49Derivation object at 0x000001A0CC9F75B0>
>>> bip49_derivation.from_address(address=10)
<hdwallet.derivations.bip49.BIP49Derivation object at 0x000001A0CC9F75B0>
>>> bip49_derivation.from_coin_type(coin_type=11)
<hdwallet.derivations.bip49.BIP49Derivation object at 0x000001A0CC9F75B0>
>>> bip49_derivation.path()
"m/49'/11'/1'/0/10"
>>> bip49_derivation.indexes()
[2147483697, 2147483659, 2147483649, 0, 10]
>>> bip49_derivation: BIP49Derivation = BIP49Derivation(coin_type=11, account=1, change=CHANGES.EXTERNAL_CHAIN, address=10)
>>> bip49_derivation.purpose()
49
>>> bip49_derivation.coin_type()
11
>>> bip49_derivation.account()
1
>>> bip49_derivation.change()
'external-chain'
>>> bip49_derivation.address()
10

.. autoclass:: hdwallet.derivations.bip84.BIP84Derivation
    :members:

>>> from hdwallet.derivations import CHANGES
>>> from hdwallet.derivations.bip84 import BIP84Derivation
>>> BIP84Derivation.name()
'BIP84'
>>> bip84_derivation: BIP84Derivation = BIP84Derivation()
>>> bip84_derivation.path()
"m/84'/0'/0'/0/0"
>>> bip84_derivation.from_coin_type(coin_type=11)
<hdwallet.derivations.bip84.BIP84Derivation object at 0x000001E9949B75B0>
>>> bip84_derivation.from_account(account=1)
<hdwallet.derivations.bip84.BIP84Derivation object at 0x000001E9949B75B0>
>>> bip84_derivation.from_change(change="external-chain")
<hdwallet.derivations.bip84.BIP84Derivation object at 0x000001E9949B75B0>
>>> bip84_derivation.from_address(address=10)
<hdwallet.derivations.bip84.BIP84Derivation object at 0x000001E9949B75B0>
>>> bip84_derivation.from_coin_type(coin_type=11)
<hdwallet.derivations.bip84.BIP84Derivation object at 0x000001E9949B75B0>
>>> bip84_derivation.path()
"m/84'/11'/1'/0/10"
>>> bip84_derivation.indexes()
[2147483732, 2147483659, 2147483649, 0, 10]
>>> bip84_derivation: BIP84Derivation = BIP84Derivation(coin_type=11, account=1, change=CHANGES.EXTERNAL_CHAIN, address=10)
>>> bip84_derivation.purpose()
84
>>> bip84_derivation.coin_type()
11
>>> bip84_derivation.account()
1
>>> bip84_derivation.change()
'external-chain'
>>> bip84_derivation.address()
10

.. autoclass:: hdwallet.derivations.bip86.BIP86Derivation
    :members:

>>> from hdwallet.derivations import CHANGES
>>> from hdwallet.derivations.bip86 import BIP86Derivation
>>> BIP86Derivation.name()
'BIP86'
>>> bip86_derivation: BIP86Derivation = BIP86Derivation()
>>> bip86_derivation.path()
"m/86'/0'/0'/0/0"
>>> bip86_derivation.from_coin_type(coin_type=11)
<hdwallet.derivations.bip86.BIP86Derivation object at 0x000001E9949B6920>
>>> bip86_derivation.from_account(account=1)
<hdwallet.derivations.bip86.BIP86Derivation object at 0x000001E9949B6920>
>>> bip86_derivation.from_change(change="external-chain")
<hdwallet.derivations.bip86.BIP86Derivation object at 0x000001E9949B6920>
>>> bip86_derivation.from_address(address=10)
<hdwallet.derivations.bip86.BIP86Derivation object at 0x000001E9949B6920>
>>> bip86_derivation.from_coin_type(coin_type=11)
<hdwallet.derivations.bip86.BIP86Derivation object at 0x000001E9949B6920>
>>> bip86_derivation.path()
"m/86'/11'/1'/0/10"
>>> bip86_derivation.indexes()
[2147483734, 2147483659, 2147483649, 0, 10]
>>> bip86_derivation: BIP86Derivation = BIP86Derivation(coin_type=11, account=1, change=CHANGES.EXTERNAL_CHAIN, address=10)
>>> bip86_derivation.purpose()
86
>>> bip86_derivation.coin_type()
11
>>> bip86_derivation.account()
1
>>> bip86_derivation.change()
'external-chain'
>>> bip86_derivation.address()
10

.. autoclass:: hdwallet.derivations.cip1852.CIP1852Derivation
    :members:

>>> from hdwallet.derivations.cip1852 import CIP1852Derivation, ROLES
>>> CIP1852Derivation.name()
'CIP1852'
>>> cip1852_derivation: CIP1852Derivation = CIP1852Derivation()
>>> cip1852_derivation.path()
"m/1852'/1815'/0'/0/0"
>>> cip1852_derivation.from_account(account=1)
<hdwallet.derivations.cip1852.CIP1852Derivation object at 0x000002601E4E4D00>
>>> cip1852_derivation.from_role(role="external-chain")
<hdwallet.derivations.cip1852.CIP1852Derivation object at 0x000002601E4E4D00>
>>> cip1852_derivation.from_address(address=10)
<hdwallet.derivations.cip1852.CIP1852Derivation object at 0x000002601E4E4D00>
>>> cip1852_derivation.path()
"m/1852'/1815'/1'/0/10"
>>> cip1852_derivation.indexes()
[2147485500, 2147485463, 2147483649, 0, 10]
>>> cip1852_derivation: CIP1852Derivation = CIP1852Derivation(account=1, role=ROLES.EXTERNAL_CHAIN, address=10)
>>> cip1852_derivation.purpose()
1852
>>> cip1852_derivation.coin_type()
1815
>>> cip1852_derivation.account()
1
>>> cip1852_derivation.role()
'external-chain'
>>> cip1852_derivation.address()
10


.. autoclass:: hdwallet.derivations.custom.CustomDerivation
    :members:

>>> from hdwallet.derivations.custom import CustomDerivation
>>> CustomDerivation.name()
'Custom'
>>> custom_derivation: CustomDerivation = CustomDerivation("m/84'/0'/1'/0/7")
>>> custom_derivation.path()
"m/84'/0'/1'/0/7"
>>> custom_derivation.indexes()
[2147483732, 2147483648, 2147483649, 0, 7]



.. autoclass:: hdwallet.derivations.electrum.ElectrumDerivation
    :members:

>>> from hdwallet.derivations.electrum import ElectrumDerivation
>>> ElectrumDerivation.name()
'Electrum'
>>> electrum_derivation: ElectrumDerivation = ElectrumDerivation()
>>> electrum_derivation.path()
'm/0/0'
>>> electrum_derivation.from_change(change=0)
<hdwallet.derivations.electrum.ElectrumDerivation object at 0x00000206B9C36E30>
>>> electrum_derivation.from_address(address=10)
<hdwallet.derivations.electrum.ElectrumDerivation object at 0x00000206B9C36E30>
>>> electrum_derivation.path()
'm/0/10'
>>> electrum_derivation.indexes()
[0, 10]
>>> electrum_derivation.change()
0
>>> electrum_derivation.address()
10


.. autoclass:: hdwallet.derivations.monero.MoneroDerivation
    :members:

>>> from hdwallet.derivations.monero import MoneroDerivation
>>> MoneroDerivation.name()
'Monero'
>>> monero_derivation: MoneroDerivation = MoneroDerivation()
>>> monero_derivation.from_major(11)
<hdwallet.derivations.monero.MoneroDerivation object at 0x0000027391CC4D00>
>>> monero_derivation.from_minor(2)
<hdwallet.derivations.monero.MoneroDerivation object at 0x0000027391CC4D00>

>>> monero_derivation: MoneroDerivation = MoneroDerivation(minor=11,major=2)
>>> monero_derivation.path()
'm/11/2'
>>> monero_derivation.indexes()
[11, 2]
>>> monero_derivation.minor()
11
>>> monero_derivation.major()
2

.. autoclass:: hdwallet.derivations.hdw.HDWDerivation
    :members:

>>> from hdwallet.derivations.hdw import HDWDerivation
>>> HDWDerivation.name()
'HDW'
>>> hdw_derivation: HDWDerivation = HDWDerivation()
>>> hdw_derivation.from_account(11)
<hdwallet.derivations.hdw.HDWDerivation object at 0x000002060AFB2130>
>>> hdw_derivation.from_address(2)
<hdwallet.derivations.hdw.HDWDerivation object at 0x000002060AFB2130>
>>> hdw_derivation: HDWDerivation = HDWDerivation(ecc='SLIP10-Ed25519-Monero')
>>> hdw_derivation.path()
"m/0'/5/0"
>>> hdw_derivation.indexes()
[2147483648, 5, 0]
>>> hdw_derivation.account()
0
>>> hdw_derivation.ecc()
'SLIP10-Ed25519-Monero'
>>> hdw_derivation.address()
0
