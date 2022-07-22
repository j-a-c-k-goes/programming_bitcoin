'''
    BITCOIN TRANSACTION HISTORY
    ---------------------------
    Program demonstrates listing history of a bitcoin.    
'''

# - - - imports - - -
from bitcoin import *

# - - - input btc address or default - - -
def btc_address():
	addr = str(input('enter a btc address (press enter to test default address):'))
	if addr == '':
		addr = '329e5RtfraHHNPKGDMXNxtuS4QjZTXqBDg' # default test
	return addr

# - - - view address transaction history - - -
def addr_history(btc_addr):
	addr_history = history(btc_addr)
	return addr_history

# - - -  function bindings - - -
btc_addr = btc_address()
history = addr_history(btc_addr)

# - - - print history of the address - - - 
print(f'''
	address\t{ history[0]["address"] }
	------------------------------------------
	value\t{ history[0]["value"] }
	------------------------------------------
	output\t{ history[0]["output"] }
	------------------------------------------
	block height\t{ history[0]["block_height"] }
	------------------------------------------
	spend\t{ history[0]["spend"] }
	''')
