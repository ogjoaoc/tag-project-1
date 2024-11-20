import networkx as nx
from scipy.io import mmread
from collections import defaultdict

MAX_NODOS = -1

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


