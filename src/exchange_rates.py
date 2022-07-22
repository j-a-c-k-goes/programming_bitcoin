'''
    BITCOIN EXCHANGE RATES FROM BLOCKCHAIN.INFO
    -------------------------------------------
    Program uses API to programmatically obtain bitcoin relevant data    
'''

# - - - imports - - -
from blockchain import exchangerates

# - - - return exchange rate data in object - - -
ticker = exchangerates.get_ticker()

# - - - get the latest exchange rates in major currencies - - -
def exchange_rates(ticker):
    print('- - - bitcoin prices in various currencies - - -')
    for key in ticker:
        # - - - p15min is minimum value - - -
        print(key, ticker[key].p15min)

# - - - convert currencies to btc - - -
def currencies_to_btc(ticker):
    for key in ticker:
        btc = exchangerates.to_btc(key, 1000)
        print(f'1000 {key} in bitcoin: {btc}')

# - - - function bindings - - -
exchange_rate = exchange_rates(ticker)
convert_to_btc = currencies_to_btc(ticker)