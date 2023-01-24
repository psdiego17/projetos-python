import requests
import json

cep = int(input('Informe o CEP que deseja obter o endereço ex: 12345000: '))

enderecoCompleto = requests.get(f'https://cep.awesomeapi.com.br/json/{cep}') #Recebendo a requisição da API
enderecoCompleto = enderecoCompleto.json() #Jogando para o formato JSON 

print(f'\nObtendo endereço do CEP : {cep}')
print('-'*30)
for c, v in enderecoCompleto.items():
    print(f'{c} = {v}')
print()           