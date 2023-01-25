from flask import Flask, jsonify, request

#Criando uma aplicação Flask, com o nome do arquivo, servidor onde vai está hospedando a API 
apiLivros = Flask(__name__)

#Base de dados local
biblioteca = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    }, 
    {
        'id': 2,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'titulo': 'James Clear',
        'autor': 'Hábitos Atômicos'
    },
]

#Consultar todos os livros
@apiLivros.route('/livros', methods=['GET'])
def buscarLivros():
    return jsonify(biblioteca)

#Consultar um livro especifico pelo id
@apiLivros.route('/livros/<int:id>', methods=['GET'])
def buscaLivroPorId(id):
    for livro in biblioteca:
        if livro.get('id') == id:
            return livro

#Editar um livro especifico pelo id
@apiLivros.route('/livros/<int:id>', methods=['PUT'])
def editarLivroPorId(id):
    livroEditado = request.get_json() #Pegar as informações que foram enviadas do usuário para API
    for indice, valor in enumerate(biblioteca):
        if valor.get('id') == id:
            biblioteca[indice].update(livroEditado)
            return jsonify(biblioteca[indice])

#Criar (Adicionar) um novo livro
@apiLivros.route('/livros', methods=['POST'])
def criarNovoLivro():
    novoLivro = request.get_json()
    biblioteca.append(novoLivro)
    return jsonify(biblioteca)

#Excluir um livro especifico pelo id
@apiLivros.route('/livros/<int:id>', methods=['DELETE'])
def deletarLivroPeloId(id):
    for indice, valor in enumerate(biblioteca):
        if valor.get('id') == id:
            del biblioteca[indice]
    return jsonify(biblioteca)        

#Iniciar à API
apiLivros.run(port=5000, host='localhost', debug=True)