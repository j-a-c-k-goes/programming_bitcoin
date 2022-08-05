'''
    STATISTICS
    -------------------------------------------
    This program uses the statistics blockchain library.    
    Note use of get() method
'''

# import library/module 
from blockchain import statistics
from operator import itemgetter

# get the stats object
stats = statistics.get()

# get bitcoin statisitics
def btc_stats(stats):
    btc_stats = {
        "trade_volume": stats.trade_volume_btc,
        "mkt_price": stats.market_price_usd,
        "total_fees": stats.total_fees_btc,
        "time_bt_blocks": stats.minutes_between_blocks,
        "btc_mined": stats.btc_mined,
        "hash_rate":stats.hash_rate,
        "next_retarget": stats.next_retarget,
        "miner_revenue_btc": stats.miners_revenue_btc,
        "num_transactions": stats.number_of_transactions,
        "difficulty": stats.difficulty,
        "block_size": stats.blocks_size,
        "est_btc_sent": stats.estimated_btc_sent
    }
    return btc_stats

# show stats
def show_stats(btc_stats):
    # can use itemgetter as alt: x, y, z = itegetter('foo', 'bar', 'baz')(dict_name)

    trade_volume, mkt_price, total_fees, time_bt_blocks, btc_mined, hash_rate, next_retarget, miners_revenue_btc, num_transactions, difficulty, blocks_size, estimated_btc_sent = btc_stats.values()
    
    output = f'''
    btc trade volume:    { trade_volume }
    btc market price:    ${ mkt_price }
    btc fees (total):    { total_fees }
    mins b/t blocks:     { time_bt_blocks }
    btc mined:           { btc_mined }
    hash rate:           { hash_rate }
    next retarget:       { next_retarget }
    miner revenue:       { miners_revenue_btc }
    no. transactions:    { num_transactions }
    difficulty:          { difficulty }
    block size:          { blocks_size }
    est. btc sent:       { estimated_btc_sent }
    '''
    print(output)
    return 0

# on run /export
if __name__ == "__main__":
    btc_stats = btc_stats(stats)
    show_stas = show_stats(btc_stats)