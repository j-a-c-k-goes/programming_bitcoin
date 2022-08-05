'''
    Block Explorer
    -------------------------------------------
    This program uses the block exploere method of the blockchain library.

    Use blockchain.info as reference site to test blocks to explore.
    https://www.blockchain.com/btc/blocks?page=1

    remember to copy the block's hash not the block's height

    broken library link: https://github.com/blockchain/api-v1-client-python

'''

# imports 
from blockchain import blockexplorer

# get a particular block
block_hash = "000000000000000000057d36eda1d7d1ec7c866a349702865b71a19718c9dc71"
block = blockexplorer.get_block(block_hash)

# display explorer results
# using length to shw number of transactions instead of window of object@ messages
print(f"""
    block fee:                 { block.fee }
    block size:                { block.size }
    block transactions:        { len(block.transactions) }
    """)

# get the latest block
block = blockexplorer.get_latest_block()

