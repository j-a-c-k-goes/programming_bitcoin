'''
    BITCOIN EXCHANGE RATES FROM BLOCKCHAIN.INFO
    -------------------------------------------
    Program uses API to programmatically obtain bitcoin relevant data    
'''

# import
from blockchain import exchangerates

# return exchange rate data in object
ticker = exchangerates.get_ticker()

# get the latest exchange rates in major currencies - - -
def exchange_rates(ticker):
    print('btc prices in various currencies')
    for key in ticker:
        # note: p15min is minimum value
        print("\t", key, ticker[key].p15min)
    print()
    return 0

# convert currencies to btc
def currencies_to_btc(ticker):
    print("btc exchange rates for various currencies\n")
    for key in ticker:
        btc = exchangerates.to_btc(key, 1000)
        # 1000 in this currency is this many btc
        print(f'\t1000 {key} in bitcoin: {btc}')
    print()
    return 0

# on run / export
if __name__ == "__main__":
    exchange_rate = exchange_rates(ticker)
    convert_to_btc = currencies_to_btc(ticker)