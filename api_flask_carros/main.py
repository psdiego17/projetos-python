from flask import Flask, request, jsonify, make_response
from bd import Carros

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

#CREATE
@app.route('/carros', methods=['POST'])
def cadastrar_carro():
    carro = request.get_json()
    Carros.append(carro)
    return make_response(
        jsonify(
            mensagem='Carro cadastrado com sucesso',
            dados=carro
        )
    )


#READ
@app.route('/carros', methods=['GET'])
def listar_carros():
    return make_response(
        jsonify(
            mensagem='Lista de carros', 
            dados=Carros
        )
    )

#READ pelo ID
@app.route('/carros/<int:id>', methods=['GET'])
def listar_carro_id(id):
    for carro in Carros:
        if carro.get('id') == id:
            return make_response(
                jsonify(
                    mensagem=f'Carro {carro["modelo"]} localizado com sucesso, seguem dados:',
                    dados=carro      
                )
            )
        else:
            return make_response(
                jsonify(
                    mensagem=f'ID informado: {id}, carro não foi localizado em nossa base'
                )
            )  


app.run(debug=True)

