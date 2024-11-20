import networkx as nx
from scipy.io import mmread
from collections import defaultdict

MAX_NODOS = -1

''' 
2*ti / (n *(n-1))
med = sum(d(vi))/max_nodos
'''
def coef_aglomeracao(adj, v):
    
    qtd_vizinhos = len(adj[v])

    if qtd_vizinhos < 2:  
        return 0.0
    
    entre_vizinho = 0

    for x in adj[v]:
        for y in adj[v]:
            if x != y and x in adj[y] and y in adj[v]:
                entre_vizinho += 1

    return entre_vizinho / ((qtd_vizinhos) * (qtd_vizinhos - 1))

def coef_aglomeracao_medio(adj):

    return sum(coef_aglomeracao(adj, v) for v in range(1, MAX_NODOS + 1)) / MAX_NODOS

def grau_por_vertice(adj):
    
    tabela = defaultdict(int)

    for nodo in range(1, MAX_NODOS + 1):
        tabela[nodo] = len(adj[nodo])
        
    return tabela

def inicializar_lista_adj(G):
    
    adj = [[] for _ in range(MAX_NODOS + 1)]
    
    for aresta in G.edges():
        u, v = aresta[0], aresta[1]
        adj[u + 1].append(v + 1)
        adj[v + 1].append(u + 1)

    return adj

matriz = mmread("soc-dolphins\\soc-dolphins.mtx")
grafo = nx.Graph(matriz)
MAX_NODOS = len(grafo.nodes())

lista_de_adj = inicializar_lista_adj(grafo)
tabela_graus_por_vertice = grau_por_vertice(lista_de_adj)

print(lista_de_adj)
print(coef_aglomeracao(lista_de_adj, 34))
print(coef_aglomeracao_medio(lista_de_adj))
print(nx.average_clustering(grafo))


