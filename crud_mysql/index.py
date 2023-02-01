import banco
import visual

while True:
    menu = ['Cadastrar Pokémon', 'Listar Pokémons', 'Buscar Pokémon',
            'Atualizar Pokémon', 'Deletar Pokémon', 'Sair']
    opcao_escolhida = visual.construir_menu(menu)

    if opcao_escolhida == 1:
        visual.construir_cabecalho('cadastrar pokémon')
        banco.criar_pokemon()

    elif opcao_escolhida == 2:
        visual.construir_cabecalho('listar pokémons')
        banco.listar_pokemons()
        
    elif opcao_escolhida == 3:
        visual.construir_cabecalho('buscar pokémon')
        banco.buscar_pokemon()

    elif opcao_escolhida == 4:
        visual.construir_cabecalho('editar pokémon')
        banco.editar_pokemon()    
    elif opcao_escolhida == 5:
        pass
    elif opcao_escolhida == 6:
        visual.construir_cabecalho('Obrigado por utilizar nossa POKEDEX')
        banco.fechar_conexao_banco()
        break
    else:
        visual.construir_cabecalho('Erro, opção inválida, informe uma opção válida')
