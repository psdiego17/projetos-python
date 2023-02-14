from flask import Flask, request, jsonify, make_response, json
import mysql.connector
from bd import Carros

#Conexão com o banco de dados

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'bd_carros',
)

#Criando cursor
my_cursor = conexao.cursor()

def fechar_conexao_banco():
    conexao.close()
    my_cursor.close()

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

#CREATE
@app.route('/carros', methods=['POST'])
def cadastrar_carro():
    
    try:
        carro = request.get_json()

        sql = f"INSERT INTO carros (marca, modelo, ano) VALUES ('{carro['marca']}', '{carro['modelo']}', {carro['ano']})"
        my_cursor.execute(sql)
        conexao.commit()
    except:
        return f'Não foi possível cadastrar o {carro["modelo"]} em nossa base'
    
    else:
        return make_response(
            jsonify(
                mensagem=f'Carro {carro["modelo"]} cadastrado com sucesso',
                dados=carro
            )
        )
    finally:
        fechar_conexao_banco()

#READ
@app.route('/carros', methods=['GET'])
def listar_carros():
    
    try:
        sql = 'SELECT * FROM carros'
        my_cursor.execute(sql)
        todos_carros = my_cursor.fetchall()
        
        resultado = list()

        for carro in todos_carros:
            #resultado = f'ID: {carro[0]}, MARCA: {carro[1]}, MODELO: {carro[2]}, ANO: {carro[3]}'
            resultado.append(
                {
                    'id': carro[0],	
                    'marca': carro[1],
                    'modelo': carro[2], 
                    'ano': carro[3]
                }
            )
    
    except:
        return f'Não foi possível carregar a lista de carros'
    
    else:
        return make_response(
            jsonify(
                mensagem='Lista de carros', 
                dados= resultado
            )
        )

#READ pelo ID
@app.route('/carros/<int:id>', methods=['GET'])
def listar_carro_id(id):
    sql = f'SELECT * FROM carros WHERE id = {id}'
    my_cursor.execute(sql)
    carro = my_cursor.fetchone() 
    
    #resposta = f'id: {carro[0]} marca: {carro[1]} modelo: {carro[2]} ano: {carro[3]}'
    try:
        if carro[0] == id:
            resposta = list()
            resposta.append(
                {
                    'id': carro[0],	
                    'marca': carro[1],
                    'modelo': carro[2], 
                    'ano': carro[3]
                }
            )
   
    except:
        return f'ID informado: {id}, carro não foi localizado em nossa base'

    else:
        return make_response(
                jsonify(
                    mensagem='Lista de carros', 
                    dados= resposta
                )
            )



if __name__ == '__main__':
    app.run(debug=True)

