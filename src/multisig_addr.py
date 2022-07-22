'''
    MULTISIGNATURE BITCOIN ADDRESS
    ------------------------------
    
    a multisignature address is associated with more than one private key.
    therefore, create at least three private keys. 
'''

# - - - imports - - -
from bitcoin import *
import time
import json

# - - - create private keys - - -
def create_private_keys(n=3):
    # - - - data holder - - -
    private_keys = []
    # - - - status update - - -
    print(f'- - - generating {n} private keys - - -')
    # - - - loop to create private keys - - -
    for i in range(n):
        key = random_key()
        private_keys.append(key)
    # - - - display created keys - - -
    for key in private_keys:
        time.sleep(1)
        print(f'private key\t{key}')
    print(f'- - - private keys generated - - -\n')
    # - - - return data - - -
    return private_keys

# - - - create public keys - - -
def public_keys(private_keys):
    public_keys = []
    print(f'- - - generating public keys from {len(private_keys)} private keys - - -')
    for priv_key in private_keys:
        pub_key = privtopub(priv_key)
        public_keys.append(pub_key)
    for key in public_keys:
        time.sleep(1)
        print(f'public key\t{key}')
    print(f'- - - public keys generated - - -\n')
    return public_keys

# - - - create multisig address from public keys - - -
def multisig_address(public_keys):
    print(f'- - - creating multisignature address from public keys - - -')
    multi_sig = mk_multisig_script(public_keys[0], public_keys[1], public_keys[2], 2, 3)
    multi_addr = scriptaddr(multi_sig)
    time.sleep(1)
    print(f'multi signature address\t{multi_addr}')
    return multi_addr

# - - - function bindings - - -
private_keys = create_private_keys(3)
public_keys = public_keys(private_keys)
multi_sig = multisig_address(public_keys)

# - - - object with private, public, and multisignature addresses - - -
priv_pub_multi = { 
    "private_keys": private_keys, 
    "public_keys": public_keys, 
    "multi_sig": multi_sig }

# - - - convert object to json - - -
object_to_json = json.dumps(priv_pub_multi, indent = 2)

# - - - write to .json file - - -
with open(".keys.json", "w") as file:
    file.write(object_to_json)
