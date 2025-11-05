:orphan:

=========
Mnemonics
=========

.. autoclass:: hdwallet.mnemonics.MNEMONICS
    :members:

>>> from hdwallet.mnemonics import MNEMONICS
>>> MNEMONICS.names()
['Algorand', 'BIP39', 'Electrum-V1', 'Electrum-V2', 'Monero']
>>> MNEMONICS.classes()
[<class 'hdwallet.mnemonics.algorand.mnemonic.AlgorandMnemonic'>, <class 'hdwallet.mnemonics.bip39.mnemonic.BIP39Mnemonic'>, <class 'hdwallet.mnemonics.electrum.v1.mnemonic.ElectrumV1Mnemonic'>, <class 'hdwallet.mnemonics.electrum.v2.mnemonic.ElectrumV2Mnemonic'>, <class 'hdwallet.mnemonics.monero.mnemonic.MoneroMnemonic'>]
>>> from hdwallet.mnemonics import BIP39Mnemonic
>>> MNEMONICS.mnemonic(name="BIP39")
<class 'hdwallet.mnemonics.bip39.mnemonic.BIP39Mnemonic'>
>>> MNEMONICS.mnemonic(name="BIP39") == BIP39Mnemonic
True
>>> MNEMONICS.is_mnemonic(name="BIP39")
True

.. autoclass:: hdwallet.mnemonics.imnemonic.IMnemonic
    :members:

.. autoclass:: hdwallet.mnemonics.algorand.mnemonic.AlgorandMnemonic
    :members:

>>> from hdwallet.mnemonics.algorand import AlgorandMnemonic, ALGORAND_MNEMONIC_WORDS, ALGORAND_MNEMONIC_LANGUAGES
>>> AlgorandMnemonic.name()
'Algorand'
>>> mnemonic: str = AlgorandMnemonic.from_words(words=ALGORAND_MNEMONIC_WORDS.TWENTY_FIVE, language=ALGORAND_MNEMONIC_LANGUAGES.ENGLISH)
>>> AlgorandMnemonic.from_entropy(entropy="65234f4ec655b087dd74d186126e301d73d563961890b2f718476e1a32522329", language=ALGORAND_MNEMONIC_LANGUAGES.ENGLISH)
'hole develop cheese fragile gaze giggle plunge sphere express reunion oblige crack priority ocean seven mosquito wagon glow castle plunge goddess stand empower ability empower'
>>> AlgorandMnemonic.encode(entropy="65234f4ec655b087dd74d186126e301d73d563961890b2f718476e1a32522329", language=ALGORAND_MNEMONIC_LANGUAGES.ENGLISH)
'hole develop cheese fragile gaze giggle plunge sphere express reunion oblige crack priority ocean seven mosquito wagon glow castle plunge goddess stand empower ability empower'
>>> mnemonic
'horse catalog image easy adult include daughter model peace correct identify buyer gravity captain grass scale jazz settle impact injury govern trumpet door above suspect'
>>> algorand_mnemonic: AlgorandMnemonic = AlgorandMnemonic(mnemonic=mnemonic)
>>> algorand_mnemonic.mnemonic()
'horse catalog image easy adult include daughter model peace correct identify buyer gravity captain grass scale jazz settle impact injury govern trumpet door above suspect'
>>> algorand_mnemonic.language()
'English'
>>> algorand_mnemonic.words()
25
>>> AlgorandMnemonic.decode(mnemonic=mnemonic)
'6efb88e25ce481c9f9868e0e250ce1f601b388bc0cc0bb1bb1e3428732a62f88'
>>> AlgorandMnemonic.is_valid_language(language="english")
True
>>> AlgorandMnemonic.is_valid_words(words=25)
True
>>> AlgorandMnemonic.is_valid(mnemonic="hole develop cheese fragile gaze giggle plunge sphere express reunion oblige crack priority ocean seven mosquito wagon glow castle plunge goddess stand empower ability empower")
True

.. autoclass:: hdwallet.mnemonics.bip39.mnemonic.BIP39Mnemonic
    :members:

>>> from hdwallet.mnemonics.bip39 import BIP39Mnemonic, BIP39_MNEMONIC_WORDS, BIP39_MNEMONIC_LANGUAGES
>>> BIP39Mnemonic.name()
'BIP39'
>>> mnemonic: str = BIP39Mnemonic.from_words(words=BIP39_MNEMONIC_WORDS.TWELVE, language=BIP39_MNEMONIC_LANGUAGES.CZECH)
>>> BIP39Mnemonic.from_entropy(entropy="1ab96e3aebfce1014e3bdddeeb7510c1", language=BIP39_MNEMONIC_LANGUAGES.CZECH)
'datel subtropy otrhat tundra synek obvod hranice nozdra uvalit lebka kajuta odeslat'
>>> BIP39Mnemonic.encode(entropy="1ab96e3aebfce1014e3bdddeeb7510c1", language=BIP39_MNEMONIC_LANGUAGES.CZECH)
'datel subtropy otrhat tundra synek obvod hranice nozdra uvalit lebka kajuta odeslat'
>>> mnemonic
'bobek soulad tabule masopust modlitba hmyz bezmoc podvod psanec hladovka nadace gramofon'
>>> bip39_mnemonic: BIP39Mnemonic = BIP39Mnemonic(mnemonic=mnemonic)
>>> bip39_mnemonic.mnemonic()
'bobek soulad tabule masopust modlitba hmyz bezmoc podvod psanec hladovka nadace gramofon'
>>> bip39_mnemonic.language()
'Czech'
>>> bip39_mnemonic.words()
12
>>> BIP39Mnemonic.decode(mnemonic=mnemonic)
'0a58af3c3326c06881ece7aa4655c497'
>>> BIP39Mnemonic.is_valid_language(language="czech")
True
>>> BIP39Mnemonic.is_valid_words(words=12)
True
>>> BIP39Mnemonic.is_valid(mnemonic="datel subtropy otrhat tundra synek obvod hranice nozdra uvalit lebka kajuta odeslat")
True

.. autoclass:: hdwallet.mnemonics.electrum.v1.mnemonic.ElectrumV1Mnemonic
    :members:

>>> from hdwallet.mnemonics.electrum.v1 import ElectrumV1Mnemonic, ELECTRUM_V1_MNEMONIC_WORDS, ELECTRUM_V1_MNEMONIC_LANGUAGES
>>> ElectrumV1Mnemonic.name()
'Electrum-V1'
>>> mnemonic: str = ElectrumV1Mnemonic.from_words(words=BIP39_MNEMONIC_WORDS.TWELVE, language=ELECTRUM_V1_MNEMONIC_LANGUAGES.ENGLISH)
>>> ElectrumV1Mnemonic.from_entropy(entropy="724bf9ce32db1baa801761c4f11fe901", language=ELECTRUM_V1_MNEMONIC_LANGUAGES.ENGLISH)
'spring hopefully foot effort complete awake stand sheep deserve any soft perfect'
>>> ElectrumV1Mnemonic.encode(entropy="724bf9ce32db1baa801761c4f11fe901", language=ELECTRUM_V1_MNEMONIC_LANGUAGES.ENGLISH)
'spring hopefully foot effort complete awake stand sheep deserve any soft perfect'
>>> mnemonic
'vast floor creation tonight company express around surface mean ode mother red'
>>> ev1_mnemonic: ElectrumV1Mnemonic = ElectrumV1Mnemonic(mnemonic=mnemonic)
>>> ev1_mnemonic.mnemonic()
'vast floor creation tonight company express around surface mean ode mother red'
>>> ev1_mnemonic.language()
'English'
>>> ev1_mnemonic.words()
12
>>> ElectrumV1Mnemonic.decode(mnemonic=mnemonic)
'9ffb4bb2ca4ae6aea3a368a3fd93ebbf'
>>> ElectrumV1Mnemonic.is_valid_language(language="english")
True
>>> ElectrumV1Mnemonic.is_valid_words(words=12)
True
>>> ElectrumV1Mnemonic.is_valid(mnemonic="spring hopefully foot effort complete awake stand sheep deserve any soft perfect")
True

.. autoclass:: hdwallet.mnemonics.electrum.v2.mnemonic.ElectrumV2Mnemonic
    :members:

>>> from hdwallet.mnemonics.electrum.v2 import ElectrumV2Mnemonic, ELECTRUM_V2_MNEMONIC_WORDS, ELECTRUM_V2_MNEMONIC_LANGUAGES, ELECTRUM_V2_MNEMONIC_TYPES
>>> ElectrumV2Mnemonic.name()
'Electrum-V2'
>>> mnemonic: str = ElectrumV2Mnemonic.from_words(words=BIP39_MNEMONIC_WORDS.TWELVE, language=ELECTRUM_V2_MNEMONIC_LANGUAGES.CHINESE_SIMPLIFIED, mnemonic_type=ELECTRUM_V2_MNEMONIC_TYPES.SEGWIT)
>>> ElectrumV2Mnemonic.from_entropy(entropy="0c3a7d6111221a9a9f3f309ee2680aa54a", language=ELECTRUM_V2_MNEMONIC_LANGUAGES.CHINESE_SIMPLIFIED)
'凭 八 响 帐 乙 牢 碗 头 术 透 德 砖'
>>> ElectrumV2Mnemonic.encode(entropy="0c3a7d6111221a9a9f3f309ee2680aa54a", language=ELECTRUM_V2_MNEMONIC_LANGUAGES.CHINESE_SIMPLIFIED, mnemonic_type=ELECTRUM_V2_MNEMONIC_TYPES.SEGWIT)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "X:\#repos\python-hdwallet\hdwallet\mnemonics\electrum\v2\mnemonic.py", line 321, in encode
    raise EntropyError("Entropy bytes are not suitable for generating a valid mnemonic")
hdwallet.exceptions.EntropyError: Entropy bytes are not suitable for generating a valid mnemonic
>>> mnemonic
'星 应 棋 翻 粗 组 路 吃 派 掷 础 鸣'
>>> ev2_mnemonic: ElectrumV2Mnemonic = ElectrumV2Mnemonic(mnemonic=mnemonic, mnemonic_type=ELECTRUM_V2_MNEMONIC_TYPES.SEGWIT)
>>> ev2_mnemonic.mnemonic()
'星 应 棋 翻 粗 组 路 吃 派 掷 础 鸣'
>>> ev2_mnemonic.language()
'Chinese-Simplified'
>>> ev2_mnemonic.words()
12
>>> ev2_mnemonic.mnemonic_type()
'segwit'
>>> ElectrumV2Mnemonic.decode(mnemonic=mnemonic, mnemonic_type=ELECTRUM_V2_MNEMONIC_TYPES.SEGWIT)
'0d04acbd49d24da36471c666f79a43436b'
>>> ElectrumV2Mnemonic.is_valid_language(language="chinese-simplified")
True
>>> ElectrumV2Mnemonic.is_valid_words(words=12)
True
>>> ElectrumV2Mnemonic.is_type(mnemonic="纠 八 响 帐 乙 牢 碗 头 术 透 德 砖", mnemonic_type=ELECTRUM_V2_MNEMONIC_TYPES.SEGWIT)
True
>>> ElectrumV2Mnemonic.is_valid(mnemonic="纠 八 响 帐 乙 牢 碗 头 术 透 德 砖", mnemonic_type=ELECTRUM_V2_MNEMONIC_TYPES.SEGWIT)
True

.. autoclass:: hdwallet.mnemonics.monero.mnemonic.MoneroMnemonic
    :members:

>>> from hdwallet.mnemonics.monero import MoneroMnemonic, MONERO_MNEMONIC_WORDS, MONERO_MNEMONIC_LANGUAGES
>>> MoneroMnemonic.name()
'Monero'
>>> mnemonic: str = MoneroMnemonic.from_words(words=BIP39_MNEMONIC_WORDS.TWELVE, language=MONERO_MNEMONIC_LANGUAGES.DUTCH)
>>> MoneroMnemonic.from_entropy(entropy="cb88cbdc872bb038f0984e611b539f03", language=MONERO_MNEMONIC_LANGUAGES.DUTCH)
'leguaan nullijn knaven pablo hekman nylon rein diode napijn tuma tout tulp'
>>> MoneroMnemonic.encode(entropy="cb88cbdc872bb038f0984e611b539f03", language=MONERO_MNEMONIC_LANGUAGES.DUTCH)
'leguaan nullijn knaven pablo hekman nylon rein diode napijn tuma tout tulp'
>>> mnemonic
'waas figurante zacharias stukadoor geslaagd lenen cuisine ultiem klagelijk zijwaarts kabinet galei'
>>> monero_mnemonic: MoneroMnemonic = MoneroMnemonic(mnemonic=mnemonic)
>>> monero_mnemonic.mnemonic()
'waas figurante zacharias stukadoor geslaagd lenen cuisine ultiem klagelijk zijwaarts kabinet galei'
>>> monero_mnemonic.language()
'Dutch'
>>> monero_mnemonic.words()
12
>>> MoneroMnemonic.decode(mnemonic=mnemonic)
'335bd0b1dce8c92aac09b99129cebbe1'
>>> MoneroMnemonic.is_valid_language(language="dutch")
True
>>> MoneroMnemonic.is_valid_words(words=13)
True
>>> MoneroMnemonic.is_valid(mnemonic="leguaan nullijn knaven pablo hekman nylon rein diode napijn tuma tout tulp nylon")
True
