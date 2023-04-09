import ccxt
import time

# definir a exchange desejada (por exemplo, Binance)
exchange = ccxt.binance({
    'rateLimit': 2000,
    'enableRateLimit': True,
})

# definir os pares de moedas desejados
symbols = ['BTC/USD', 'BNB/USD', 'BNB/BRL']

while True:
    for symbol in symbols:
        ticker = exchange.fetch_ticker(symbol)
        price = ticker['last']
        print(f'Preço atual de {symbol} na {exchange.name}: {price}')
    time.sleep(60) # espera 1 minuto antes de atualizar novamente
