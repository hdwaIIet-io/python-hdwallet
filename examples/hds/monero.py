#!/usr/bin/env python3

from hdwallet.hds import MoneroHD
from hdwallet.derivations import MoneroDerivation
from hdwallet.cryptocurrencies import Monero

monero_hd: MoneroHD = MoneroHD(
    network=Monero.NETWORKS.MAINNET, minor=1, major=0
)

seed = "7700d24525cd55c703aa3bf96590938b60d6408d6c56cc1d6d28bdb4d768b893"
private_key = "ab37a127a265102d9910702a41eefd879adedec8de3f2f9142b6d3361df3323d"
spend_private_key = "228d2d013851b0ae7a26873e92c7bccf5fd6408d6c56cc1d6d28bdb4d768b803"
view_private_key = "b80a6f3f4d679d5c4ebfd59eb15bab9247c1322473954594173bd3f6f9c78503"
spend_public_key = "18e3d47a702c21c23a27bd397c77bebc248ef1c06d010b0cd8a557c44acf818e"
payment_id = "ad17dc6e6793d178"

monero_hd.from_seed(seed=seed)
# monero_hd.from_private_key(private_key=private_key)
# monero_hd.from_spend_private_key(spend_private_key=spend_private_key)
# monero_hd.from_watch_only(
#     view_private_key=view_private_key, spend_public_key=spend_public_key
# )

print("Seed:", monero_hd.seed())
print("Private Key:", monero_hd.private_key())
print("Spend Private Key:", monero_hd.spend_private_key())
print("View Private Key:", monero_hd.view_private_key())
print("Spend Public Key:", monero_hd.spend_public_key())
print("View Public Key:", monero_hd.view_public_key())
print("Primary Address:", monero_hd.primary_address())

print("Payment ID:", payment_id)
print("Integrated Address:", monero_hd.integrated_address(payment_id))

monero_derivation: MoneroDerivation = MoneroDerivation(
    minor=1, major=0
)
monero_hd.from_derivation(monero_derivation)

print("Sub-Address:", monero_hd.sub_address())
