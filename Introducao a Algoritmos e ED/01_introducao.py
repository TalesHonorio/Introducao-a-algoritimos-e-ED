# Introdução a Algoritmos e Estruturas de Dados

"""
Disciplina: Introdução a Algoritmos e Estrutura de Dados
Objetivo: Apresentar os conceitos básicos de algoritmos, estratégias de resolução de problemas e estruturas de dados fundamentais.
Este material serve como base para a primeira aula.
"""

# ---------------------------------------
# 1. O que é um Algoritmo?
# ---------------------------------------
"""
Definição:
Um algoritmo é uma sequência finita de passos bem definidos para resolver um problema.

Exemplos de algoritmos na vida real:
- Receita de bolo
- Manual de instruções
- Lista de passos para encontrar um endereço

Características de um algoritmo:
1. Finitude (tem que terminar)
2. Entrada (dados iniciais)
3. Saída (resultado esperado)
4. Clareza (instruções bem definidas)
"""

# Exemplo simples de algoritmo: Somar dois números
def soma(a, b):
    return a + b

print("Exemplo de Algoritmo - Soma de dois números:", soma(3, 5))

# ---------------------------------------
# 2. Estratégias de Design de Algoritmos
# ---------------------------------------
"""
Existem diferentes formas (estratégias) de criar algoritmos para resolver problemas.
Algumas das principais são:

1. Brute Force (Força Bruta)
--------------------------------
- Ideia: Tentar todas as possibilidades até encontrar a solução.
- Quando usar: Problemas pequenos ou quando nenhuma outra solução é óbvia.
- Exemplos do dia a dia:
  - Procurar uma senha testando todas as combinações possíveis.
  - Achar um número específico olhando um por um em uma lista bagunçada.

2. Decrease and Conquer (Diminuir e Conquistar)
-----------------------------------------------
- Ideia: Reduzir o problema a uma versão menor dele mesmo e resolver passo a passo.
- Quando usar: Quando o problema pode ser quebrado de forma simples em versões menores.
- Exemplos:
  - Busca Binária: A cada passo, você corta a lista pela metade.
  - Contagem regressiva: Resolver o problema para N, depois para N-1, N-2, e assim por diante.

3. Divide and Conquer (Dividir e Conquistar)
---------------------------------------------
- Ideia: Dividir o problema em vários subproblemas independentes, resolver cada um e depois juntar as soluções.
- Quando usar: Quando as partes podem ser resolvidas separadamente e combinadas depois.
- Exemplos:
  - Merge Sort: Divide a lista em duas partes, ordena cada uma e depois junta.
  - Quick Sort: Escolhe um pivô, separa os menores e os maiores, e ordena recursivamente.

4. Transform and Conquer (Transformar e Conquistar)
---------------------------------------------------
- Ideia: Modificar os dados de entrada para facilitar a solução do problema.
- Quando usar: Quando uma transformação prévia deixa o problema mais fácil de resolver.
- Exemplos:
  - Ordenar uma lista antes de aplicar uma busca eficiente.
  - Converter uma matriz para outra estrutura antes de fazer cálculos.

5. Dynamic Programming (Programação Dinâmica)
---------------------------------------------
- Ideia: Resolver subproblemas menores, guardar os resultados e reutilizar quando necessário.
- Quando usar: Quando o problema tem subproblemas repetitivos e sobrepostos.
- Exemplos:
  - Fibonacci com memoização.
  - Problema da Mochila (Knapsack Problem).
  - Cálculo de caminhos mínimos em grafos.

6. Greedy (Guloso)
-------------------
- Ideia: Tomar a melhor decisão local em cada passo, esperando que isso leve a uma solução global boa.
- Quando usar: Quando o problema tem a chamada "propriedade gulosa", ou seja, decisões locais levam à melhor solução global.
- Exemplos:
  - Problema do Troco: Escolher sempre a maior moeda possível.
  - Algoritmo de Kruskal para encontrar a Árvore Geradora Mínima.

"""

# ---------------------------------------
# 3. Estruturas de Dados Fundamentais
# ---------------------------------------
"""
Estruturas básicas usadas para armazenar e organizar dados:

- Listas (Arrays)
- Pilhas (Stacks)
- Filas (Queues)
- Conjuntos (Sets)
- Dicionários (Maps / HashMaps)

Exemplos teóricos:

1. Listas (Arrays)
- Permitem acessar elementos por índice.
- Úteis para armazenar sequências de dados.

2. Pilhas (Stacks)
- Seguem o princípio LIFO (Last In, First Out / Último a entrar, primeiro a sair).
- Exemplo da vida real: Uma pilha de pratos.

3. Filas (Queues)
- Seguem o princípio FIFO (First In, First Out / Primeiro a entrar, primeiro a sair).
- Exemplo da vida real: Fila de banco ou fila do cinema.

4. Conjuntos (Sets)
- Estrutura que não permite elementos duplicados.
- Útil para verificar rapidamente se um item já existe ou não.

5. Dicionários (Maps / HashMaps)
- Permitem armazenar pares chave-valor.
- Exemplo: Agenda de contatos (nome -> telefone).

"""

# ---------------------------------------
# 4. Principais Problemas Computacionais
# ---------------------------------------
"""
Agora vamos falar de alguns dos principais tipos de problemas que você vai encontrar ao estudar algoritmos:

1. Problemas de Busca
- Exemplo: Procurar um nome específico em uma lista de contatos.
- Algoritmos típicos: Busca Linear, Busca Binária.

2. Problemas de Ordenação
- Exemplo: Organizar uma lista de alunos em ordem alfabética.
- Algoritmos típicos: Bubble Sort, Selection Sort, Quick Sort, Merge Sort.

3. Contagem de Ocorrências
- Exemplo: Saber quantas vezes uma palavra aparece em um texto.
- Algoritmos típicos: Uso de dicionários para contagem.

4. Problemas em Grafos
- Exemplo: Encontrar o caminho mais curto entre duas cidades.
- Algoritmos típicos: Dijkstra, BFS (Busca em Largura), DFS (Busca em Profundidade).

5. Problemas de Otimização
- Exemplo: Como encher uma mochila com itens de maior valor sem ultrapassar o peso máximo.
- Algoritmos típicos: Programação Dinâmica, Algoritmos Gulosos.

6. Problemas de Caminhamento ou Percurso
- Exemplo: Robô que precisa percorrer um labirinto.
- Algoritmos típicos: BFS, DFS, A* (A-estrela).

7. Problemas de Alocação de Recursos
- Exemplo: Como agendar aulas para não ter conflitos de horário.
- Algoritmos típicos: Algoritmos de escalonamento.

"""

"""
Este material cobre conceitos introdutórios.
Nas próximas aulas, cada um desses tópicos pode ser explorado com mais profundidade!
Lembre-se: entender algoritmos e estruturas de dados é como aprender a resolver problemas de forma organizada e eficiente.
É a base para se tornar um bom programador!
"""
