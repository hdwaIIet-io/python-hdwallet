#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

import inspect
# Import the module containing cryptocurrency definitions
from bip38 import cryptocurrencies

# The original 'try/except from .. import environment' block was removed. 
# It was likely causing ImportError when run as a script and was not used 
# later in the code, leading to an unnecessary silent error handler.

# Define a dictionary to map cryptocurrency class names to their classes.
# The variable name uses snake_case as it represents a module-level collection,
# not a globally immutable constant (though convention often leans toward ALL_CAPS
# for module-level variables like this if they are treated as immutable).
bip38_cryptocurrencies = {
    # Iterate over all members of the 'cryptocurrencies' module
	name: cls for name, cls in inspect.getmembers(cryptocurrencies, inspect.isclass)
    # Filter to include only classes that inherit from ICryptocurrency
    # and exclude the base interface class itself (ICryptocurrency).
    if issubclass(cls, cryptocurrencies.ICryptocurrency) and cls is not cryptocurrencies.ICryptocurrency
}

# Example of how the dynamically loaded data is structured:
# print(bip38_cryptocurrencies)

# If the file needs to execute specific logic when run directly:
if __name__ == "__main__":
    # Placeholder for execution logic if this file is run as a script.
    print(f"Loaded {len(bip38_cryptocurrencies)} cryptocurrency handlers.")
