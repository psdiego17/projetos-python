def construir_cabecalho(texto):
    print()
    print('-'*30,f'{texto}'.center(10).upper(),'-'*30)

def construir_menu(lista):
    cont = 1
    construir_cabecalho('MENU PRINCIPAL')
    for l in (lista):
        print(f'{cont} - {l}')
        cont += 1
    opcao = int(input('Opção: '))
    return opcao
