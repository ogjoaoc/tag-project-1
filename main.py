import networkx as nx
import random
import matplotlib.pyplot as plt
import sys
from scipy.io import mmread
from collections import defaultdict
from os import system, name
sys.dont_write_bytecode = True

'''
main.py
Projeto 1 - Teoria e Aplicação de Grafos.
Autores: João Carlos (232009511) e Ricardo Nabuco (231021360).
Professor: Díbio.
'''

def inicializar_lista_adj(G):               # Contrução de uma lista de adjacências a partir do grafo.
    
    adj = [[] for _ in range(MAX_NODOS + 1)]        
    
    for aresta in G.edges():                # Adiciona as conexões de cada aresta à lista de adjacências.
        u, v = aresta[0], aresta[1]
        adj[u + 1].append(v + 1)
        adj[v + 1].append(u + 1)

    return adj

def grau_por_vertice(adj):                  # Calcula o grau de cada vértice.
    
    tabela = defaultdict(int)               # Dicionário com o grau de cada vértice. 

    for nodo in range(1, MAX_NODOS + 1):    # Conta o número de vizinhos de cada vértice.
        tabela[nodo] = len(adj[nodo])
        
    for nodo, grau in tabela.items():
        print(f"Vértice: {nodo} - Grau: {tabela[nodo]}")

def bron_kerbosch(C, P, E, cliques):

    '''
    Algoritmo de Bron-Kerborsch:
    C - Vértices do clique que está sendo feito.
    P - Candidatos a participar do clique
    E - Nós que já foram processados.
    cliques - Lista com os cliques maximais.
    Fonte: slides da disciplina (Aula 5).
    '''

    if not P and not E:
        cliques.append(C)
        return
    
    for candidato in list(P):
        bron_kerbosch(C.union({candidato}), P.intersection(set(grafo.neighbors(candidato))), E.intersection(set(grafo.neighbors(candidato))), cliques)
        P.remove(candidato)
        E.add(candidato)

def encontrar_cliques_maximais(grafo):      # Função para encontrar os cliques maximais utilizando o Algoritmo de Bron Kerbosch.

    cliques_maximais = []
    bron_kerbosch(set(), set(grafo.nodes()), set(), cliques_maximais)  

    print("\nCliques Maximais:")   

    for i in range(0, len(cliques_maximais)):
        print(f"Clique {i + 1} ({len(cliques_maximais[i])} vértices): {cliques_maximais[i]}")
    
    return cliques_maximais

def coef_aglomeracao(adj, v):               # Calcula o coeficiente de aglomeração para o vértice v.
    
    qtd_vizinhos = len(adj[v])              # Número de vizinhos do vértice.

    if qtd_vizinhos < 2:                    # Se o vértice não tem no mínimo dois vizinhos, não há triângulos. 
        return 0.0
    
    entre_vizinho = 0                       # Contador para conexões entre vizinhos.

    for x in adj[v]:                        # Loop para verificar pares de vizinhos do vértice v.
        for y in adj[v]:
            if x != y and x in adj[y] and y in adj[v]:
                entre_vizinho += 1

    return entre_vizinho / ((qtd_vizinhos) * (qtd_vizinhos - 1))       

def coef_aglomeracao_medio(adj):            # Função para calcular o coeficiente de aglomeração médio do grafo.

    return sum(coef_aglomeracao(adj, v) for v in range(1, MAX_NODOS + 1)) / MAX_NODOS  

def print_coef_alomeracao_por_vertice():    # Módulo para impressão dos vértices e seus respectivos coeficientes de aglomeração.

    for i in range(1, MAX_NODOS + 1):
        print(f'Vértice: {i} - Coeficiente: {coef_aglomeracao(lista_de_adj, i)}')

def visualizar_grafo_com_cliques(grafo, cliques):    

    pos = nx.spring_layout(grafo)           # Definir um layout para posicionar os nós no grafo. 
    
    clique_colors = [f"#{random.randint(0, 0xFFFFFF):06x}" for _ in range(len(cliques))]    # Gerar cores únicas para cada clique maximal.

    colors = {}

    for i in range(len(cliques)):           # Mapear as cores para os nós, com uma cor padrão para nós fora de cliques.
        for no in cliques[i]:
            colors[no] = clique_colors[i]
            
    default_color = "#cccccc"               # Definição cor padrão (cinza) para nós que não pertencem a cliques destacados.
    node_colors = [colors.get(node, default_color) for node in grafo.nodes()]

    nx.draw(grafo, pos, with_labels=True, node_color=node_colors, edge_color="#999999", node_size=500, font_size=10)
    plt.gcf().canvas.manager.set_window_title("Visualização do Grafo - Cliques maximais destacados por cores") 
    plt.show()

def menu():                                 # Módulo para inicializar menu do programa.

    from dependencies.menu import inicio  
    inicio()

def limpar_terminal():                     # Módulo para flush do terminal.

    if name == 'nt':                       # Alterna entre diferentes sistemas operacionais.
        _ = system('cls')
    else:
        _ = system('clear')



matriz = mmread("soc-dolphins\\soc-dolphins.mtx")    # Carrega a matriz do arquivo.

grafo = nx.Graph(matriz)                    # Construção do grafo usando NetworkX.

MAX_NODOS = len(grafo.nodes())              # Definição do número total de nós.

lista_de_adj = inicializar_lista_adj(grafo) # Construção da Lista de adjacências.

if __name__ == "__main__":
    menu() 



