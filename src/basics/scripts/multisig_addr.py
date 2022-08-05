'''
    MULTISIGNATURE BITCOIN ADDRESS
    ------------------------------
    a multisignature address is associated 
    with more than one private key
    and requires least three private keys to generate.
'''

# imports
from bitcoin import *
from datetime import datetime
import json

# define private keys, default is 3 
def create_private_keys(n=3):
    private_keys = list()
    print(f'generating {n} private keys')

    # create the keys w/ a loop
    for i in range(n):
        key = random_key()
        private_keys.append(key)

    # loop through created keys, print results 
    for key in private_keys:
        time.sleep(1)
        print(f'private key\t{key}')
    
    print(f'\nprivate keys generated\n')
    return private_keys

# define public keys from private keys
def public_keys(private_keys):
    public_keys = list()
    print(f'generating public keys from {len(private_keys)} private keys')

    for priv_key in private_keys:
        pub_key = privtopub(priv_key)
        public_keys.append(pub_key)
    
    for key in public_keys:
        time.sleep(1)
        print(f'public key\t{key}')
    
    print(f'\npublic keys generated\n')
    return public_keys

# create multisig address from public keys 
def multisig_address(public_keys):
    print(f'creating multisignature address from public keys')
    multi_sig = mk_multisig_script(public_keys[0], public_keys[1], public_keys[2], 2, 3)
    multi_addr = scriptaddr(multi_sig)
    time.sleep(1)
    print(f'multi signature address\t{multi_addr}')
    return multi_addr

# organize private, public, and multisignature addresses into object
def priv_pub_multi(private_keys, public_keys, multi_sig):
    priv_pub_multi = { 
        "private_keys": private_keys,
        "public_keys": public_keys, 
        "multi_sig": multi_sig 
        }
    return priv_pub_multi

# convert object to json
def convert_to_json(obj):
    print("converting data to json format")
    object_to_json = json.dumps(obj, indent = 2)
    return object_to_json
    print("complete!")

# write to .json file
def write_to_json(obj):
    output_as = ".keys.json"
    print("writing data to .json format")
    with open(output_as, "w") as file:
        file.write(obj)
    print("complete!")

# on run / export 
if __name__ == "__main__":
    private_keys = create_private_keys(3)
    public_keys = public_keys(private_keys)
    multi_sig = multisig_address(public_keys)
    priv_pub_multi = priv_pub_multi(private_keys, public_keys, multi_sig)
    convert_to_json = convert_to_json(priv_pub_multi)
    write_to_json = write_to_json(convert_to_json)
