'''
    HELLO BITCOIN
    -------------
    program demonstrates creation of:
    - private keys
    - public keys
    - bitcoin address

    private_key generates 
    public_key which generates
    btc_address

    note: always use a different btc address per transaction
'''

# - - - imports - - -
from bitcoin import *

# - - - generate a private key - - -
private_key = random_key()

# - - - display private key - - -
print(f'private key\t{private_key}')

# - - - create public key using private key - - -
public_key = privtopub(private_key)

# - - - display public key - - -
print(f'public key\t{public_key}')

# - - - generate a bitcoin address - - -
btc_addr = pubtoaddr(public_key)

# - - - display bitcoin address - - -
print(f'btc address\t{btc_addr}')
