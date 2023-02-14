import requests

def requisicao(moeda_base, valor_base, moeda_desejada):
    url = requests.get(f'https://api.exchangerate.host/latest?base={moeda_base}').json()
    return obter_dados_cotacao(url)

def obter_dados_cotacao(url):
    valor_moeda_desejada = url['rates']
    cotacao_moeda_desejada = valor_moeda_desejada.get(moeda_desejada)

    print(f'\n1 {moeda_base} vale {cotacao_moeda_desejada:.2f} {moeda_desejada}')

    return converter_moedas(cotacao_moeda_desejada)


def converter_moedas(cotacao_moeda_desejada):
    valor_convertido = valor_base * cotacao_moeda_desejada
    return f'{valor_base} {moeda_base} equivale a {valor_convertido:.2f} {moeda_desejada}'

    
moeda_base = str(input('Informe a moeda base USD, BRL, EUR: ')).strip().upper()
valor_base = float(input('Informe o valor que deseja cambiar: '))
moeda_desejada = str(input('Informe a moeda desejada USD, BRL, EUR: ')).strip().upper()

print(requisicao(moeda_base, valor_base, moeda_desejada))