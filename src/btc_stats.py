'''
    STATISTICS
    -------------------------------------------
    This program uses the statistics blockchain library.    
    Note use of get() method
'''

# - - - import library/module - - -
from blockchain import statistics

# - - - get the stats object - - -
stats = statistics.get()

# - - - get and print bitcoin trade volume (a statistic) - - -
def btc_stats(stats):
    trade_volume = stats.trade_volume_btc
    mkt_price = stats.market_price_usd
    total_fees = stats.total_fees_btc
    time_bt_blocks = stats.minutes_between_blocks
    btc_mined = stats.btc_mined
    hash_rate = stats.hash_rate

    output = f'''
    btc trade volume\t{ trade_volume }
    btc market price\t{ mkt_price }
    btc fees (total)\t{ total_fees }
    mins b/t blocks\t{ time_bt_blocks }
    btc mined\t{ btc_mined }
    hash rate\t{ hash_rate }
    '''

    print(output)
    return [trade_volume,mkt_price,total_fees,time_bt_blocks,btc_mined,hash_rate]

btc_stats = btc_stats(stats)