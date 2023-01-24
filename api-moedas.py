import requests
import json

cotacoes = requests.get(' https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes = cotacoes.json()
#print(cotacoes)
cotacaoDolar = cotacoes['USDBRL']['bid']
print(f'\nCotação do dólar USD {cotacaoDolar}\n')

for c, v in cotacoes.items():
    for c2, v2 in v.items():
        print(f'{c2} = {v2}')
    print()    