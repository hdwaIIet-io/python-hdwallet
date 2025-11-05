:orphan:

=====
Seeds
=====

.. autoclass:: hdwallet.seeds.SEEDS
    :members:

>>> from hdwallet.seeds import SEEDS
>>> SEEDS.names()
['Algorand', 'BIP39', 'Cardano', 'Electrum-V1', 'Electrum-V2', 'Monero']
>>> SEEDS.classes()
[<class 'hdwallet.seeds.algorand.AlgorandSeed'>, <class 'hdwallet.seeds.bip39.BIP39Seed'>, <class 'hdwallet.seeds.cardano.CardanoSeed'>, <class 'hdwallet.seeds.electrum.v1.ElectrumV1Seed'>, <class 'hdwallet.seeds.electrum.v2.ElectrumV2Seed'>, <class 'hdwallet.seeds.monero.MoneroSeed'>]
>>> from hdwallet.seeds import BIP39Seed
>>> SEEDS.seed(name="Algorand")
<class 'hdwallet.seeds.algorand.AlgorandSeed'>
>>> SEEDS.seed(name="BIP39")
<class 'hdwallet.seeds.bip39.BIP39Seed'>
>>> SEEDS.seed(name="BIP39") == BIP39Seed
True
>>> SEEDS.is_seed(name="Electrum-V2")
True

.. autoclass:: hdwallet.seeds.iseed.ISeed
    :members:

.. autoclass:: hdwallet.seeds.algorand.AlgorandSeed
    :members:

>>> from hdwallet.seeds.algorand import AlgorandSeed
>>> AlgorandSeed.from_mnemonic(mnemonic="outer special dice battle mouse afraid half nut marble reason journey north hole measure mango cargo learn actress slogan analyst lunar marriage gaze above twelve")
'ea3cf47a345148120cad973dc4ecf06459b627e6b022f6b3c09785804221168c'
>>> algorand_seed: AlgorandSeed = AlgorandSeed(seed="ea3cf47a345148120cad973dc4ecf06459b627e6b022f6b3c09785804221168c")
>>> algorand_seed.name()
'Algorand'
>>> algorand_seed.seed()
'ea3cf47a345148120cad973dc4ecf06459b627e6b022f6b3c09785804221168c'




.. autoclass:: hdwallet.seeds.bip39.BIP39Seed
    :members:

>>> from hdwallet.seeds.bip39 import BIP39Seed
>>> bip39_seed.from_mnemonic(mnemonic="인생 생활 일반 통계 근육 근래 기온 사랑 관심 양주 국제 피아노")
'b43f7e1a19a71f3fab6f7a125e3c1c11789c1144a91c480928f1bdf48e083e623db7ff6abf865696388899cd49d7299601bba77afd95d1c0bfe897284aaadda2'
>>> bip39_seed: BIP39Seed = BIP39Seed(seed="b43f7e1a19a71f3fab6f7a125e3c1c11789c1144a91c480928f1bdf48e083e623db7ff6abf865696388899cd49d7299601bba77afd95d1c0bfe897284aaadda2")
>>> bip39_seed.name()
'BIP39'
>>> bip39_seed.seed()
'b43f7e1a19a71f3fab6f7a125e3c1c11789c1144a91c480928f1bdf48e083e623db7ff6abf865696388899cd49d7299601bba77afd95d1c0bfe897284aaadda2'


.. autoclass:: hdwallet.seeds.cardano.CardanoSeed
    :members:

>>> from hdwallet.seeds.cardano import CardanoSeed
>>>CardanoSeed.from_mnemonic(mnemonic="возраст чушь целевой клоун колено кисть против заснуть шоколад хулиган готовый шумно")
'1d9eb3c129f55ca568f20ff85df8ac7c'
>>> cardano_seed: CardanoSeed = CardanoSeed(seed="1d9eb3c129f55ca568f20ff85df8ac7c")
>>> cardano_seed.name()
'Cardano'
>>> cardano_seed.seed()
'1d9eb3c129f55ca568f20ff85df8ac7c'
>>> cardano_seed.generate_byron_icarus(mnemonic="возраст чушь целевой клоун колено кисть против заснуть шоколад хулиган готовый шумно")
'1d9eb3c129f55ca568f20ff85df8ac7c'
>>> cardano_seed.generate_byron_ledger(mnemonic="возраст чушь целевой клоун колено кисть против заснуть шоколад хулиган готовый шумно")
'638a38b69826d3f43539061739363c45b1bc8831c2c0c6f94e2e66e1e3d56de9fdfa86d53615b3c98df4f12de384c3b392e156689d66a2d51759d66422b17117'
>>> cardano_seed.generate_byron_legacy(mnemonic="возраст чушь целевой клоун колено кисть против заснуть шоколад хулиган готовый шумно")
'bf4c9d6ffb5dc8e958f3e545ed2cb0dabbd4cefce4b9e89d70a95aae45aa102e'
>>> cardano_seed.generate_shelley_icarus(mnemonic="возраст чушь целевой клоун колено кисть против заснуть шоколад хулиган готовый шумно")
'1d9eb3c129f55ca568f20ff85df8ac7c'
>>> cardano_seed.generate_shelley_ledger(mnemonic="возраст чушь целевой клоун колено кисть против заснуть шоколад хулиган готовый шумно")
'638a38b69826d3f43539061739363c45b1bc8831c2c0c6f94e2e66e1e3d56de9fdfa86d53615b3c98df4f12de384c3b392e156689d66a2d51759d66422b17117'

.. autoclass:: hdwallet.seeds.electrum.v1.ElectrumV1Seed
    :members:

>>>from hdwallet.seeds.electrum.v1 import ElectrumV1Seed
>>>ElectrumV1Seed.from_mnemonic(mnemonic="stretch sister juice brother youth egg salt join lesson cover grin journey")
'98cc82dcea53272eb75f244a38b93b0e182ef4c7c0ca012b6b4622c970f5842b'
>>>electrumv1_seed: ElectrumV1Seed = ElectrumV1Seed(seed="98cc82dcea53272eb75f244a38b93b0e182ef4c7c0ca012b6b4622c970f5842b")
>>>electrumv1_seed.name()
'Electrum-V1'
>>> electrumv1_seed.seed()
'98cc82dcea53272eb75f244a38b93b0e182ef4c7c0ca012b6b4622c970f5842b'


.. autoclass:: hdwallet.seeds.electrum.v2.ElectrumV2Seed
    :members:

>>> from hdwallet.seeds.electrum.v2 import ElectrumV2Seed
>>> ElectrumV2Seed.from_mnemonic(mnemonic="servo privado viaduto caixote agachar inspetor albergue seleto cuspir apontar obedecer tacho")
'a15b1990667046d688eb0fed7fd8789487c0b919dff86778bf31b5abb83a5d8471bcc9d4a1d2f97eef84ab334bbb30804b4001f73ae7b02353c1e2040f758bb5'
>>> electrumv2_seed: ElectrumV2Seed = ElectrumV2Seed(seed="a15b1990667046d688eb0fed7fd8789487c0b919dff86778bf31b5abb83a5d8471bcc9d4a1d2f97eef84ab334bbb30804b4001f73ae7b02353c1e2040f758bb5")
>>> electrumv2_seed.name()
'Electrum-V2'
>>> electrumv2_seed.seed()
'a15b1990667046d688eb0fed7fd8789487c0b919dff86778bf31b5abb83a5d8471bcc9d4a1d2f97eef84ab334bbb30804b4001f73ae7b02353c1e2040f758bb5'

.. autoclass:: hdwallet.seeds.monero.MoneroSeed
    :members:

>>> from hdwallet.seeds.monero import MoneroSeed
>>> MoneroSeed.from_mnemonic(mnemonic="签 箱 些 芽 企 靠 除 森 页 摇 降 咱")
'14910059f5fa36208f3f431447a7037e'
>>>monero_seed: MoneroSeed = MoneroSeed(seed="14910059f5fa36208f3f431447a7037e")
>>> monero_seed.name()
'Monero'
>>> monero_seed.seed()
'14910059f5fa36208f3f431447a7037e'
