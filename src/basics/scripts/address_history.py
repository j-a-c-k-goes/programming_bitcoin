'''
    BITCOIN TRANSACTION HISTORY
    ---------------------------
    Program demonstrates listing history of a bitcoin.    
'''

# imports
from bitcoin import *

# input btc address or default
def btc_address():
	addr = str(input('enter a btc address (press enter to test default address):'))
	if addr == '':
		try:
			print("nothing entered. using default address")
			addr = '329e5RtfraHHNPKGDMXNxtuS4QjZTXqBDg' # default test
		except ValueError:
			print("you probably entered an invalid address or an empty string with spaces.")
			print("exiting")
			exit()
	return addr

# view address transaction history
def addr_history(btc_addr):
	try:
		addr_history = history(btc_addr)
	except:
		print("there does not appear to be any history associated with this address")
	return addr_history

# show history associated with the address
def show_history(addr_history):
	for addr in addr_history:
		print(f"""
address:        { addr["address"] }
value:          { addr["value"] }
output:         { addr["output"] }
block height:   { addr["block_height"] }
""")
		# below key sometimes broken when using 
		#spend:          { addr["spend"] }
	return 0

# on run / export
if __name__ == "__main__":
    btc_addr = btc_address()
    history = addr_history(btc_addr)
    show_history = show_history(history)