# Estruturas de Dados - Aula 5

"""
Disciplina: Introdução a Algoritmos e Estruturas de Dados
Tema: Grafos

Conteúdo:
- Definições
- Exemplos do mundo real
- Propriedades e tipos de grafos
- Representação computacional de grafos
- Busca em grafos (DFS e BFS)
- Variações de grafos e terminologia
- Aplicações práticas
- Exercícios
"""

# --------------------------------------------
# Definições
# --------------------------------------------
"""
Um grafo G é uma estrutura matemática que representa um conjunto de objetos (vértices ou nós) e as conexões entre eles (arestas ou ligações).

Formalmente:
G = (V, E)
- V é o conjunto de vértices: V = {v1, v2, ..., vn}
- E é o conjunto de arestas: E = {e1, e2, ..., em}, onde cada aresta conecta dois vértices

Tipos de Grafos:
- Grafo Direcionado (ou dígrafo): as arestas têm direção. Se (u,v) ∈ E, então vai de u para v, mas não necessariamente de v para u.
- Grafo Não Direcionado: as arestas não têm direção. Se (u,v) ∈ E, então (v,u) ∈ E também.

Grafos podem ser:
- Simples: não possuem laços (aresta de um vértice para ele mesmo) nem múltiplas arestas entre dois vértices.
- Multigrafos: permitem múltiplas arestas entre dois vértices.
- Ponderados: cada aresta possui um valor associado (custo, tempo, distância, etc).
- Acíclicos: não possuem ciclos (caminho fechado).
- Conectados: existe um caminho entre qualquer par de vértices.

Conceitos adicionais:
- Caminho: sequência de vértices conectados por arestas.
- Ciclo: caminho que começa e termina no mesmo vértice.
- Vértice isolado: não possui arestas conectando a ele.
- Componente conexa: subgrafo no qual todos os vértices estão conectados entre si.
"""

# --------------------------------------------
# Exemplos do mundo real
# --------------------------------------------
"""
Grafos são extremamente úteis para modelar relações complexas entre entidades:

1. Redes Sociais:
   - Usuários são vértices
   - Conexões (amizades, seguidores) são arestas
   - Direcionado ou não, dependendo da plataforma (Instagram é dirigido, Facebook não)

2. Sistemas de Transporte:
   - Cidades são vértices
   - Estradas ou rotas são arestas (com pesos indicando distância ou tempo)

3. Redes de Computadores:
   - Dispositivos como nós
   - Conexões físicas ou lógicas como arestas

4. Roteamento de Pacotes:
   - Encontrar o caminho de menor custo (em tempo ou distância) entre origem e destino

5. Análise de dependências:
   - Tarefas de um projeto como nós
   - Dependência entre elas como arestas direcionadas (DAGs)

6. Grafos na IA:
   - Grafos de busca em jogos (ex: labirintos, xadrez)
   - Representação de problemas de raciocínio lógico
"""

# --------------------------------------------
# Propriedades e conceitos
# --------------------------------------------
"""
1. Grau:
   - Em grafos não direcionados: número de arestas conectadas ao vértice
   - Em grafos direcionados:
       - Grau de entrada (in-degree): número de arestas que chegam ao vértice
       - Grau de saída (out-degree): número de arestas que saem do vértice

2. Caminhos:
   - Caminho simples: não repete vértices
   - Caminho mais curto: menor número de arestas (ou menor custo)

3. Ciclos:
   - Simples: não repete vértices, exceto o primeiro/último
   - Grafos acíclicos: não contêm ciclos (ex: DAGs)

4. Conectividade:
   - Um grafo é conectado se há caminho entre qualquer par de vértices
   - Componentes conexas: subconjuntos de vértices que são conectados entre si, mas desconectados do restante do grafo

5. Grafos completos:
   - Cada vértice está conectado com todos os outros
   - Um grafo completo com n vértices possui n(n-1)/2 arestas (não direcionado)
"""

# --------------------------------------------
# Representação Computacional
# --------------------------------------------
"""
1. Lista de Adjacência:
   - Representa o grafo como um dicionário (ou lista) onde cada chave é um vértice e o valor é a lista de vizinhos.
   - Vantagens:
       - Uso eficiente de memória em grafos esparsos
       - Acesso rápido aos vizinhos
   - Desvantagens:
       - Verificar se um vértice está conectado a outro pode ser O(n)

2. Matriz de Adjacência:
   - Matriz booleana ou de inteiros onde posição [i][j] = 1 (ou peso) se há aresta de i para j
   - Vantagens:
       - Verificação imediata da existência de conexão
       - Útil para algoritmos baseados em matrizes (ex: multiplicação de caminhos)
   - Desvantagens:
       - Ocupa mais espaço (O(n²)) mesmo em grafos esparsos

3. Lista de arestas:
   - Lista de tuplas: (u, v) ou (u, v, peso)
   - Útil para algoritmos baseados em arestas (Kruskal, por exemplo)
"""

# --------------------------------------------
# Busca em Grafos
# --------------------------------------------
"""
1. BFS - Breadth-First Search (Busca em Largura):
   - Estratégia de visita por "camadas"
   - Explora todos os vizinhos antes de ir para o próximo nível
   - Ideal para descobrir o caminho mais curto em grafos não ponderados
   - Utiliza fila (queue) como estrutura auxiliar

2. DFS - Depth-First Search (Busca em Profundidade):
   - Estratégia de "mergulho": explora o caminho até o fim antes de retroceder
   - Útil para detectar ciclos, componentes conexas, e ordenações topológicas
   - Implementada via recursão ou pilha (stack)

Diferenças:
- BFS usa fila, DFS usa pilha
- BFS tende a ser melhor para caminhos mínimos
- DFS é mais natural para verificação de propriedades estruturais
"""

from collections import deque

def bfs(grafo, inicio):
    visitados = set()
    fila = deque([inicio])
    while fila:
        vertice = fila.popleft()
        if vertice not in visitados:
            print(vertice, end=' ')
            visitados.add(vertice)
            fila.extend(v for v in grafo[vertice] if v not in visitados)

def dfs(grafo, inicio, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(inicio)
    print(inicio, end=' ')
    for vizinho in grafo[inicio]:
        if vizinho not in visitados:
            dfs(grafo, vizinho, visitados)

grafo_exemplo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("\nBusca em Largura (BFS):")
bfs(grafo_exemplo, 'A')

print("\n\nBusca em Profundidade (DFS):")
dfs(grafo_exemplo, 'A')

# --------------------------------------------
# Variações e Terminologia
# --------------------------------------------
"""
- DAG (Directed Acyclic Graph): grafo direcionado e sem ciclos
  - Muito utilizado em análise de dependências e ordenação de tarefas

- Subgrafo: parte de um grafo contendo subconjunto de vértices e arestas

- Caminho mínimo: menor caminho entre dois nós, considerando custo das arestas (ex: Dijkstra, Bellman-Ford)

- Árvores: são grafos especiais, conectados e acíclicos, com n vértices e n-1 arestas
"""

# --------------------------------------------
# Exercícios Propostos
# --------------------------------------------
"""
1) Crie um grafo não-direcionado representando uma rede de amigos com pelo menos 5 pessoas.
   a) Implemente a busca em largura a partir de uma das pessoas.

2) Dado um grafo direcionado representando dependências entre tarefas:
   Tarefas: A -> B, A -> C, B -> D, C -> D
   a) Represente esse grafo em lista de adjacência
   b) Faça a busca em profundidade a partir de 'A'

3) Qual a diferença prática entre lista de adjacência e matriz de adjacência?

4) Dado o grafo:
    A -- B
    |    |
    C -- D
   a) Mostre a matriz de adjacência correspondente
   b) Qual o grau de cada vértice?

5) Descreva uma aplicação prática onde seria preferível usar matriz de adjacência.

6) Adicione pesos nas arestas do grafo do exercício 2 e represente como matriz de adjacência ponderada.

7) Implemente uma função que detecte ciclos em grafos direcionados.
"""

"""
Na próxima aula, estudaremos algoritmos clássicos sobre grafos (Dijkstra, Kruskal, Prim, etc).
"""
