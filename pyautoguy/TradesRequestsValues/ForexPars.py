import requests
import json

url = "https://economia.awesomeapi.com.br/all/USD-BRL,EUR-BRL,BTC-BRL"

response = requests.get(url)

data = json.loads(response.text)

for currency, value in data.items():
    print(f'{currency}:')
    print(f'\tÚltima atualização: {value["create_date"]}')
    print(f'\tCompra: {value["bid"]}')
    print(f'\tVenda: {value["ask"]}')
