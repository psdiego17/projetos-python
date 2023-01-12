import PySimpleGUI as l
from math import pow

layoutTela = [
    [l.Text('Altura')],
    [l.Input(key='altura')],
    [l.Text('Peso')],
    [l.Input(key='peso')],
    [l.Button('calcular'), l.Button('limpar')],
    [l.Text('', key='resultado')],
]

janela = l.Window('Calculadora IMC', layout=layoutTela)

while True:
    event, values = janela.read()
    if event == l.WIN_CLOSED:
        break
    if event == 'calcular':
        altura = float(values['altura'])
        peso = float(values['peso'])
        
        imc = (peso/(pow(altura,2)))

        if imc > 0:
            if(imc <= 18.4):
                resultado = 'Abaixo do peso!'
            elif((imc >= 18.5) and (imc <= 24.9)):
                resultado = 'com o Peso ideal!'
            elif ((imc >= 25) and (imc <= 29.9)):
                resultado = 'com Sobrepeso!'
            elif((imc >= 30) and (imc <= 39.9)):
                resultado = 'com Obesidade'
            else:
                resultado = 'com Obesidade Mórbida!'
            janela['resultado'].update(f'Seu IMC é: {imc:.2f}, você está: {resultado}')
    if event == 'limpar':
        janela.close()
janela.close()            
