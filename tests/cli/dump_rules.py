bip_44_to_bip_144_rule = {
        "available-methods": {
            "entropy": {
                "method": "entropy",
                "derivable": True,
            },
            "mnemonic": {
                "method": "mnemonic",
                "derivable": True
            },
            "seed": {
                "method": "seed",
                "derivable": True,
                "root-changes": {
                    "entropy": None,
                    "strength": None,
                    "mnemonic": None,
                    "passphrase": None,
                    "language": None
                }
            },
            "xprivate-key": {
                "method": "root_xprivate_key",
                "derivable": True,
                "root-changes": {
                    "entropy": None,
                    "strength": None,
                    "mnemonic": None,
                    "passphrase": None,
                    "language": None,
                    "seed": None
                }
            },
            "wif": {
                "method": "wif",
                "derivable": False,
                "root-changes": {
                    "entropy": None,
                    "strength": None,
                    "mnemonic": None,
                    "passphrase": None,
                    "language": None,
                    "seed": None,
                    "root_xprivate_key": None,
                    "root_xpublic_key": None,
                    "root_private_key": None,
                    "root_wif": None,
                    "root_chain_code": None,
                    "root_public_key": None,
                    "strict": None
                },
                "derivation-changes": {
                    "xprivate_key": None,
                    "xpublic_key": None,
                    "chain_code": None,
                    "parent_fingerprint": None
                }
            },
            "private-key": {
                "method": "private_key",
                "derivable": False,
                "root-changes": {
                    "entropy": None,
                    "strength": None,
                    "mnemonic": None,
                    "passphrase": None,
                    "language": None,
                    "seed": None,
                    "root_xprivate_key": None,
                    "root_xpublic_key": None,
                    "root_private_key": None,
                    "root_wif": None,
                    "root_chain_code": None,
                    "root_public_key": None,
                    "strict": None
                },
                "derivation-changes": {
                    "xprivate_key": None,
                    "xpublic_key": None,
                    "chain_code": None,
                    "parent_fingerprint": None
                }
            },
            "public-key": {
                "method": "public_key",
                "derivable": False,
                "root-changes": {
                    "entropy": None,
                    "strength": None,
                    "mnemonic": None,
                    "passphrase": None,
                    "language": None,
                    "seed": None,
                    "root_xprivate_key": None,
                    "root_xpublic_key": None,
                    "root_private_key": None,
                    "root_wif": None,
                    "root_chain_code": None,
                    "root_public_key": None,
                    "wif_type": None,
                    "strict": None
                },
                "derivation-changes": {
                    "xprivate_key": None,
                    "xpublic_key": None,
                    "private_key": None,
                    "chain_code": None,
                    "wif": None,
                    "parent_fingerprint": None
                }
            }
        },
        "args": {
            "public-key-type": "public_key_type",
            "language": "language"
        }
    }

rules = {
    "BIP32" : {
        "available-methods": {
            "entropy": {
                "method": "entropy",
                "derivable": True,
            },
            "mnemonic": {
                "method": "mnemonic",
                "derivable": True
            },
            "seed": {
                "method": "seed",
                "derivable": True,
                "root-changes": {
                    "entropy": None,
                    "strength": None,
                    "mnemonic": None,
                    "passphrase": None,
                    "language": None
                }
            },
            "xprivate-key": {
                "method": "root_xprivate_key",
                "derivable": True,
                "root-changes": {
                    "entropy": None,
                    "strength": None,
                    "mnemonic": None,
                    "passphrase": None,
                    "language": None,
                    "seed": None
                }
            },
            "xpublic-key": {
                "method": "root_xpublic_key",
                "derivable": True,
                "root-changes": {
                    "entropy": None,
                    "strength": None,
                    "mnemonic": None,
                    "passphrase": None,
                    "language": None,
                    "seed": None,
                    "root_xprivate_key": None,
                    "root_private_key": None,
                    "root_wif": None,
                    "wif_type": None
                },
                "derivation-changes": {
                    "xprivate_key": None,
                    "private_key": None,
                    "wif": None
                }
            },
            "wif": {
                "method": "wif",
                "derivable": False,
                "root-changes": {
                    "entropy": None,
                    "strength": None,
                    "mnemonic": None,
                    "passphrase": None,
                    "language": None,
                    "seed": None,
                    "root_xprivate_key": None,
                    "root_xpublic_key": None,
                    "root_private_key": None,
                    "root_wif": None,
                    "root_chain_code": None,
                    "root_public_key": None,
                    "strict": None
                },
                "derivation-changes": {
                    "xprivate_key": None,
                    "xpublic_key": None,
                    "chain_code": None,
                    "parent_fingerprint": None
                }
            },
            "private-key": {
                "method": "private_key",
                "derivable": False,
                "root-changes": {
                    "entropy": None,
                    "strength": None,
                    "mnemonic": None,
                    "passphrase": None,
                    "language": None,
                    "seed": None,
                    "root_xprivate_key": None,
                    "root_xpublic_key": None,
                    "root_private_key": None,
                    "root_wif": None,
                    "root_chain_code": None,
                    "root_public_key": None,
                    "strict": None
                },
                "derivation-changes": {
                    "xprivate_key": None,
                    "xpublic_key": None,
                    "chain_code": None,
                    "parent_fingerprint": None
                }
            },
            "public-key": {
                "method": "public_key",
                "derivable": False,
                "root-changes": {
                    "entropy": None,
                    "strength": None,
                    "mnemonic": None,
                    "passphrase": None,
                    "language": None,
                    "seed": None,
                    "root_xprivate_key": None,
                    "root_xpublic_key": None,
                    "root_private_key": None,
                    "root_wif": None,
                    "root_chain_code": None,
                    "root_public_key": None,
                    "wif_type": None,
                    "strict": None
                },
                "derivation-changes": {
                    "xprivate_key": None,
                    "xpublic_key": None,
                    "private_key": None,
                    "chain_code": None,
                    "wif": None,
                    "parent_fingerprint": None
                }
            }
        },
        "args": {
            "public-key-type": "public_key_type",
            "language": "language"
        }
    },
    "BIP44" : bip_44_to_bip_144_rule,
    "BIP49" : bip_44_to_bip_144_rule,
    "BIP84" : bip_44_to_bip_144_rule,
    "BIP86" : bip_44_to_bip_144_rule,
    "Cardano": {
        "available-methods": {
            "entropy": {
                "method": "entropy",
                "derivable": True,
            },
            "mnemonic": {
                "method": "mnemonic",
                "derivable": True
            },
            "seed": {
                "method": "seed",
                "derivable": True,
                "root-changes": {
                    "entropy": None,
                    "strength": None,
                    "mnemonic": None,
                    "passphrase": None,
                    "language": None
                }
            },
            "xprivate-key": {
                "method": "root_xprivate_key",
                "derivable": True,
                "root-changes": {
                    "entropy": None,
                    "strength": None,
                    "mnemonic": None,
                    "passphrase": None,
                    "language": None,
                    "seed": None
                }
            }
        },
        "args": {
            "cardano-type": "cardano_type",
            "language": "language",
            "seed-client": ("Cardano",),
            # "address-type": ("staking",)
        }
    },
    "Electrum-V1": {
        "available-methods": {
            "entropy": {
                "method": "entropy",
                "derivable": True,
            },
            "mnemonic": {
                "method": "mnemonic",
                "derivable": True
            },
            "seed": {
                "method": "seed",
                "derivable": True,
                "root-changes": {
                    "entropy": None,
                    "strength": None,
                    "mnemonic": None,
                    "passphrase": None,
                    "language": None
                }
            },
            "wif": {
                "method": "master_wif",
                "derivable": True,
                "root-changes": {
                    "entropy": None,
                    "strength": None,
                    "mnemonic": None,
                    "passphrase": None,
                    "language": None,
                    "seed": None
                }
            },
            "private-key": {
                "method": "master_private_key",
                "derivable": True,
                "root-changes": {
                    "entropy": None,
                    "strength": None,
                    "mnemonic": None,
                    "passphrase": None,
                    "language": None,
                    "seed": None
                }
            }
        },
        "args": {
            "public-key-type": "public_key_type",
            "entropy-client": ("Electrum-V1",),
            "mnemonic-client": ("Electrum-V1",),
            "seed-client": ("Electrum-V1",),
            "language": "language"
        }
    },
    "Electrum-V2": {
        "available-methods":{
            "entropy": {
                "method": "entropy",
                "derivable": True,
            },
            "mnemonic": {
                "method": "mnemonic",
                "derivable": True
            },
            "seed": {
                "method": "seed",
                "derivable": True,
                "root-changes": {
                    "entropy": None,
                    "strength": None,
                    "mnemonic": None,
                    "passphrase": None,
                    "language": None
                }
            }
        },
        "args": {
            "mnemonic-type": "mnemonic_type",
            "mode": "mode",
            "entropy-client": ("Electrum-V2",),
            "mnemonic-client": ("Electrum-V2",),
            "seed-client": ("Electrum-V2",),
            "language": "language"
        }
    },
    "Monero": {
        "available-methods": {
            "entropy": {
                "method": "entropy",
                "derivable": True,
            },
            "mnemonic": {
                "method": "mnemonic",
                "derivable": True
            },
            "seed": {
                "method": "seed",
                "derivable": True,
                "root-changes": {
                    "entropy": None,
                    "strength": None,
                    "mnemonic": None,
                    "passphrase": None,
                    "language": None
                }
            },
            "spend-private-key": {
                "method": "spend_private_key",
                "derivable": True,
                "root-changes": {
                    "entropy": None,
                    "strength": None,
                    "mnemonic": None,
                    "passphrase": None,
                    "language": None,
                    "seed": None
                }
            }
        },
        "args": {
            "language": "language",
            "network": "network",
            "entropy-client": ("Monero",),
            "mnemonic-client": ("Monero",),
            "seed-client": ("Monero",),
            "payment-id": ("ad17dc6e6793d178",)
        }
    }
}
