valores = [100, 200, 300, 400, 500]

'''
r = Usado somente para ler algo
w = Usado somente para escrever algo, sempre apaga tudo e sobrescreve
r+ = Usado para ler e escrever algo
a = Usado para acrescentar algo
'''

'''
#O comando with open('meu_arquivo.txt') vai criar um arquivo .txt caso ainda não exista
with open('numeros.txt', 'w') as arquivo:
    for v in valores:
        arquivo.write(str(v) + '\n') #Convertendo para uma string
'''

'''
#Adicionar dado no arquivo .txt sempre no final da lista
with open('numeros.txt', 'a') as arquivo:
    arquivo.write(str(600) + '\n')
    #for v in valores:
    #    arquivo.write(str(v) + '\n')
'''

#Lendo os dados salvos no .txt
with open('numeros.txt', 'r') as arquivo:
    for v in arquivo:
        print(v)


'''
#Ler dados do arquivo .txt e salvar dado
with open('numeros.txt', 'r+') as arquivo:
    for v in arquivo:
        print(v)
    arquivo.write(str(700) + '\n')
'''