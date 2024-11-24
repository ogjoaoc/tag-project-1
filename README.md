# Teoria e Aplicação de Grafos - Projeto 1.

---

## Autores

**Alunos:**
Ricardo de Carvalho Nabuco (231021360) e João Carlos Gonçalves (232009511).<br>
**Professor:** Díbio.   
**Semestre:** 2024/2.

---

## Descrição

Este projeto consiste na aplicação prática de conceitos da matéria de Teoria e Aplicação de Grafos, focando na análise e manipulação de grafos através de algoritmos e da linguagem Python. Foi implementado o Algoritmo de Bron-Kerbosch para encontrar cliques maximais, como também módulos para cálculo de coeficientes de aglomeração e graus dos vértices.

A aplicação trabalha com os dados da base soc-dolphins, um grafo que representa interações sociais entre golfinhos. O programa identifica os cliques maximais, calcula propriedades do grafo e garante a visualização com destaque para os cliques maximais encontrados.

---

## Como Executar

 ### Pré-requisitos

  Com o Python 3.9+ instalado:

 1. Clone este repositório para a sua máquina local:
    ```bash
    git clone https://github.com/ogjoaoc/tag-project-1.git
    cd tag-project-1
    ```

 2. Instale as dependências do projeto:
    ```bash
    pip install -r dependencies/setup.txt
    ```
### Executando o Projeto

 1. Certifique-se de que **soc-dolphins.mtx** está na pasta do projeto, no caminho indicado pelo script (exemplo: `soc-dolphins/soc-dolphins.mtx`).
   
 2. Execute o programa principal:
    ```bash
    python main.py
    ```
---

## Tecnologias Utilizadas

- Python 3.9+.
- NetworkX: Biblioteca para manipulação de grafos.
- Matplotlib: Biblioteca para visualização.
- SciPy: Para leitura da matriz de adjacência do arquivo soc-dolphins.mtx.

---

## Visualização

É possível selecionar uma opção para visualização do grafo completo, que destaca as cores dos cliques maximais (com sobreposições).

![Previa_grafo](https://media.discordapp.net/attachments/1191933282032549908/1310313578833903659/image.png?ex=6744c41d&is=6743729d&hm=f3e3c2bbce6747ef18ed5811dc6b91e273848bc729e62f7dc5278542cbfe23ba&=&format=webp&quality=lossless&width=1335&height=676)


---

