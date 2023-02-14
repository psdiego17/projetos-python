import requests

class Pokemon:
    def __init__(self, nome, id, tipo, altura, peso, habilidades, golpes):
        self.nome = nome
        self.id = id
        self.tipo = tipo
        self.altura = altura
        self.peso = peso
        self.habilidades = habilidades
        self.golpes = golpes

#Função que faz a requisição da url da API
def buscarPokemon(pokemon):
    try:
        url = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}').json()

    except requests.RequestException:
        print(f'\033[31mERRO! Pokemon não localizado\033[m') 
    
    else:
        if pokemon != '':  
            return dadosPokemon(url)
        else:
            print(f'\033[31mERRO! Pokemon não informado\033[m') 
#Função que carrega os dados principais
def dadosPokemon(url):
    golpes = []
    habilidades = []
    
    for t in url['types']:
        tipo = t['type']['name']

    for a in url['abilities']:
        habilidades.append(a['ability']['name'])

    for g in url['moves']:
        golpes.append(g['move']['name'])

    #Criação do objeto pokemon do tipo pokemon
    pokemon  = Pokemon(url["name"], url["id"], tipo, url["height"], url["weight"], habilidades, golpes)    
    
    return pokedex(pokemon)

#Função para mostrar os dados principais do pokemon, CUSTOMIZAR
def pokedex(dados):
    print('-'*10,f'POKEDEX'.center(10), '-'*10)
    print(f'NOME: {dados.nome}')
    print(f'#ID: {dados.id}')
    print(f'TIPO: {dados.tipo}')
    print(f'ALTURA: {dados.altura}')
    print(f'PESO: {dados.peso}')
    print(f'HABILIDADES: {dados.habilidades}')
    print(f'GOLPES: {dados.golpes}')
    print('-'*30)

while True:
    nome_pokemon = str(input('Nome ou número do Pokémon: ')).strip().lower()
    buscarPokemon(nome_pokemon)

    while True:
        opcao = str(input('Deseja verificar outro Pokemon? [S/N] ')).strip().upper()[0]
        if opcao in 'SsNn':
            break
    if opcao in 'Nn':
        break
print(f'\033[32mObrigado por utilizar a pokedex\033[m')