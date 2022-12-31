from random import choice
computador = choice(['Pedra', 'Papel', 'Tesoura']).upper()
humano = str(input('Escolha Pedra, Papel ou Tesoura: ')).strip().upper()
resultado = ''

if((humano == 'PEDRA' and computador == 'TESOURA') or (humano == 'PAPEL' and computador == 'PEDRA') or (humano == 'TESOURA' and computador == 'PAPEL')):
    resultado = '\033[0;32;43mPARABÉNS! VOCÊ GANHOU!!!\033[m'
elif(humano == computador):
    resultado = '\033[0;36;30mEMPATOU\033[m'
else:
    resultado = '\033[0;31;40mCOMPUTADOR VENCEU!\033[m'
print(f'PC = {computador} x HUMANO = {humano}\n{resultado}')