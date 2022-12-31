nome = str(input('Informe o seu nome: ')).strip().upper()
altura = float(input('Informe a sua altura ex: 170: '))
pesoAtual = round(float(input('Informe o seu peso atual ex 67.9: ')))
sexo = (input('Informe o seu sexo H ou M: '))

pesoIdeal = 0
pesoIdealAjustado = 0

if(sexo == 'H' or sexo == 'h'):
    pesoIdeal = (52 + (0.75 * (altura - 152.4)))
elif(sexo == 'M' or sexo == 'm'):
    pesoIdeal = (52 + (0.67 * (altura - 152.4)))

pesoIdealAjustado = (((pesoAtual - pesoIdeal) * 0.25) + pesoIdeal)
print(f'Olá {nome}, seu peso ideal é: {pesoIdeal:.2f}Kg, e o seu peso ideal ajustado é: {pesoIdealAjustado:.2f}kg')
