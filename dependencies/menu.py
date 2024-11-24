from main import *

'''
menu.py
Projeto 1 - Teoria e Aplicação de Grafos.
Autores: João Carlos (232009511) e Ricardo Nabuco (231021360).
Professor: Díbio.
'''

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
        print("(5) Visualização do grafo completo (indexado em 0, vértices : [0, 61]).")
        print("(6) Sair.")
        
        while True:

            print("Selecione a opção desejada: ")
            
            try:
                opcao = int(input())
                break
            except:
                limpar_terminal()
                print("A opção deve ser um número inteiro válido, de 1 a 6.")
                print()
                skip = input("Digite enter para tentar novamente...")
                limpar_terminal()

            
        limpar_terminal()

        match opcao:
            case 1:
                grau_por_vertice(lista_de_adj)
            case 2:
                encontrar_cliques_maximais(grafo)
            case 3:
                print_coef_alomeracao_por_vertice()
            case 4:
                print()
                print(f'Coeficiente médio de aglomeração: {coef_aglomeracao_medio(lista_de_adj)}')
            case 5:
                visualizar_grafo_com_cliques(grafo, encontrar_cliques_maximais(grafo)) # Visualização do grafo com os cliques destacados.
            case 6:
                break
            case _:
                print()
                print("Opção inválida! Selecione novamente uma opção.")
        
        print()
        skip = input("Digite enter para continuar...")
        limpar_terminal()