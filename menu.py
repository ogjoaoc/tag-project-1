from main import *

def inicio():
    while True:
        print()
        print("Bem-vindo usuário!")
        print()
        print("Visualização dos dados soc-dolphins, seleciona uma opção:")
        print("(1) Todos os vértices do grafo e seus respectivos graus.")
        print("(2) Todos os cliques maximais.")
        print("(3) O coeficiente de Aglomeração de todos vértices do grafo.")
        print("(4) O coeficiente médio de Aglomeração.")
        print("(5) Visualização do grafo completo.")
        print("(6) Sair.")
        
        print()
        opcao = int(input("Selecione a opção desejada: "))
        limpar_terminal()

        match opcao:
            case 1:
                print(tabela_graus_por_vertice)
            case 2:
                encontrar_cliques_maximais(grafo)
            case 3:
                for i in range(1, MAX_NODOS + 1):
                    print(f'Vértice: {i} - {coef_aglomeracao(lista_de_adj, i)}')
            case 4:
                print(coef_aglomeracao_medio(lista_de_adj))
            case 5:
                cliques_maximais = encontrar_cliques_maximais(grafo) # Encontrar os cliques maximais no grafo
                visualizar_grafo_com_cliques(grafo, cliques_maximais) # Visualização do grafo com os cliques destacados.
            case 6:
                break
            case _:
                print()
                print("Opção inválida! Selecione novamente uma opção.")
        
        print()
        skip = input("Digite enter para continuar...")
        limpar_terminal()