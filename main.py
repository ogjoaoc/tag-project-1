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

    pos = nx.spring_layout(grafo)   # Definir um layout para posicionar os nós no grafo. 
    
    clique_colors = [f"#{random.randint(0, 0xFFFFFF):06x}"
                    for _ in range(len(cliques))]    # Gerar cores únicas para cada clique maximal.

    colors = {}
    for i, clique in enumerate(cliques):    # Mapear as cores para os nós, com uma cor padrão para nós fora de cliques.
        for node in clique:
            colors[node] = clique

    default_color = "#cccccc"        # Definição cor padrão (cinza) para nós que não pertencem a cliques destacados
    node_colors = [colors.get(node, default_color) for node in grafo.nodes()]

    nx.draw(            # Desenho do Grafo.
        grafo,
        pos,
        with_labels=True,
        node_color=node_colors,
        edge_color="#999999",
        node_size=500,
        font_size=10,
    )
    plt.title("Grafo com Cliques Destacados")
    plt.show()

matriz = mmread("soc-dolphins\\soc-dolphins.mtx")    # Carrega a matriz do arquivo no formato Matrix Market.
grafo = nx.Graph(matriz)     # Construção do grafo usando NetworkX.
MAX_NODOS = len(grafo.nodes())    # Definição do número total de nós.

lista_de_adj = inicializar_lista_adj(grafo) # Construção da Lista de adjacências.
tabela_graus_por_vertice = grau_por_vertice(lista_de_adj)    # Cálculo dos graus de cada vértice.

print(lista_de_adj) # Impressão da lista de Adjacências
print(coef_aglomeracao(lista_de_adj, 34)) # Impressão do vértice 34 e seu coeficiente de aglomeração.
print(coef_aglomeracao_medio(lista_de_adj)) # Impressão do coeficiente de aglomeração médio. 
print(nx.average_clustering(grafo)) # Impressão do coeficiente médio.

def encontrar_cliques_maximais(grafo):    # Função para os cliques maximais
    """
    Exibir todos os cliques maximais no grafo.
    grafo (networkx.Graph): Grafo carregado no NetworkX.
    list: Lista de cliques maximais, onde cada clique é representado por uma lista de nós.
    """
    
    cliques_maximais = list(nx.find_cliques(grafo))    # Encontrar os cliques maximais usando NetworkX

    print("\nCliques Maximais:") # Exibição dos cliques encontrados.

    for i, clique in enumerate(cliques_maximais, start=1):
        print(f"Clique {i} ({len(clique)} vértices): {clique}")

    return cliques_maximais

cliques_maximais = encontrar_cliques_maximais(grafo) # Encontrar os cliques maximais no grafo.

visualizar_grafo_com_cliques(grafo, cliques_maximais) # Visualização do grafo com os cliques destacados.
