import mysql.connector
import visual

#Conexão com o banco de dados
conexao = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='root',
    database='bd_pokedex',
)
   
#Inicia a conexão com o banco de dados
cursor = conexao.cursor()

def fechar_conexao_banco():
    cursor.close()
    conexao.close()


#CREATE
def criar_pokemon():
    nome_pokemon = str(input('Nome do Pokémon: ')).strip().lower()
    id_pokemon = int(input('ID do Pokémon: '))
    tipo_pokemon = str(input('Tipo do Pokémon: ')).strip().lower()
    altura_pokemon = float(input('Altura do Pokémon: '))
    peso_pokemon = float(input('Peso do Pokémon: '))

    try:
        query = f'INSERT INTO pokemons (nome_pokemon, id_pokemon, tipo_pokemon, altura_pokemon, peso_pokemon) VALUES ("{nome_pokemon}", {id_pokemon}, "{tipo_pokemon}", {altura_pokemon}, {peso_pokemon})'
        cursor.execute(query)
        conexao.commit()

    except mysql.connector.Error:
        print(f'\nNão foi possível salvar o pokémon {nome_pokemon} no banco')

    else:
        print(f'\nPokémon {nome_pokemon} salvo com sucesso!')

#READ
def listar_pokemons():
    cont = 0
    try:
        query = f'SELECT * FROM pokemons'
        cursor.execute(query)
        pokemons = cursor.fetchall()

    except mysql.connector.Error:
        print(f'\nNão foi possível listar so pokémons')

    else:
        for p in pokemons:
            print(f'NOME: {p[1]},\nNº: {p[2]},\nTIPO: {p[3]},\nALTURA {p[4]}m,\nPESO: {p[5]}Kg')
            print()

#READ PELO ID
def buscar_pokemon():
    dado_pokemon = (input('Nome ou ID do Pokémon: '))
    
    try:
        query = f'SELECT * FROM pokemons WHERE nome_pokemon = "{dado_pokemon}" OR id_pokemon = "{dado_pokemon}"'
        cursor.execute(query)
        pokemon = cursor.fetchone() #cursor.fetchone() pegar um único registro

    except mysql.connector.Error:
        print(f'\nNão foi possível localizar o pokémon')

    else:
        print(f'\nNOME: {pokemon[1].upper()},\nNº: {pokemon[2]},\nTIPO: {pokemon[3]},\nALTURA {pokemon[4]}m,\nPESO: {pokemon[5]}Kg')

#UPDATE
def editar_pokemon():
    pass