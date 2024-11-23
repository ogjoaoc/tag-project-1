import networkx as nx
from scipy.io import mmread
from collections import defaultdict

MAX_NODOS = -1        # Variável global para o número máximo de nós no grafo.

''' 
2*ti / (n *(n-1))
med = sum(d(vi))/max_nodos
'''
def coef_aglomeracao(adj, v):         # Calcula o coeficiente de aglomeração para o vértice v.
    
    qtd_vizinhos = len(adj[v])        # Número de vizinhos do vértice.

    if qtd_vizinhos < 2:              # Se o vértice não tem no mínimo dois vizinhos, não há triângulos. 
        return 0.0
    
    entre_vizinho = 0                 # Contador para conexões entre vizinhos.

    for x in adj[v]:                  # Loop para verificar pares de vizinhos do vértice v.
        for y in adj[v]:
            if x != y and x in adj[y] and y in adj[v]:
                entre_vizinho += 1

    return entre_vizinho / ((qtd_vizinhos) * (qtd_vizinhos - 1))           # Retorna o coeficiente de aglomeração.

def coef_aglomeracao_medio(adj):      # Função para calcular o coeficiente de aglomeração médio do grafo.

    return sum(coef_aglomeracao(adj, v) for v in range(1, MAX_NODOS + 1)) / MAX_NODOS  # Soma os coeficientes de todos os vértices e divide pelo número total de nós.

def grau_por_vertice(adj):          # Calcula o grau de cada vértice.
    
    tabela = defaultdict(int)       # Dicionário com o grau de cada vértice. 

    for nodo in range(1, MAX_NODOS + 1):  # Conta o número de vizinhos de cada vértice.
        tabela[nodo] = len(adj[nodo])
        
    return tabela

def inicializar_lista_adj(G):        # Contrução de uma lista de adjacências a partir do grafo.
    
    adj = [[] for _ in range(MAX_NODOS + 1)]        # Cria uma lista de adjacências para todos os nós.
    
    for aresta in G.edges():         # Adiciona as conexões de cada aresta à lista de adjacências.
        u, v = aresta[0], aresta[1]
        adj[u + 1].append(v + 1)
        adj[v + 1].append(u + 1)

    return adj

def visualizar_grafo_com_cliques(grafo, cliques):    # Gerar uma visualizaação do grafo com cliques destacados com cores.

    pos = nx.spring_layout(grafo)
    

matriz = mmread("soc-dolphins\\soc-dolphins.mtx")
grafo = nx.Graph(matriz)
MAX_NODOS = len(grafo.nodes())

lista_de_adj = inicializar_lista_adj(grafo)
tabela_graus_por_vertice = grau_por_vertice(lista_de_adj)

print(lista_de_adj)
print(coef_aglomeracao(lista_de_adj, 34))
print(coef_aglomeracao_medio(lista_de_adj))
print(nx.average_clustering(grafo))


