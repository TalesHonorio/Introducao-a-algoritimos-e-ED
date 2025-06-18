# Estruturas de Dados Lineares - Aula 3

"""
Disciplina: Introdução a Algoritmos e Estruturas de Dados
Tema: Estruturas de Dados Lineares

Nesta aula vamos estudar as principais estruturas de dados lineares: Arrays, Listas Ligadas, Filas, Pilhas e Matrizes.
Vamos comparar, entender vantagens e desvantagens e ver exemplos práticos.
"""

# --------------------------------------------
# Arrays
# --------------------------------------------
"""
O que é um Array?
- Estrutura que armazena elementos em posições contíguas de memória.
- Acesso rápido por índice (tempo constante O(1)).

Características:
- Tamanho fixo (em muitas linguagens como C, Java).
- Todos os elementos são do mesmo tipo.

Exemplo de uso:
- Armazenar notas de alunos.
- Lista de temperaturas do mês.

Pseudocódigo para acessar o terceiro elemento:
array[2]

Exemplo em Python (listas se comportam como arrays dinâmicos):
"""

temperaturas = [20, 22, 24, 21, 19]
print("Temperatura do terceiro dia:", temperaturas[2])

# --------------------------------------------
# Listas Ligadas (Linked Lists)
# --------------------------------------------
"""
Definição:
- Estrutura onde cada elemento (nó) aponta para o próximo.
- Não ocupam posições contíguas na memória.

Vantagens:
- Fácil inserção e remoção de elementos.
- Não precisa saber o tamanho total na criação.

Desvantagens:
- Acesso sequencial (não é possível acessar direto por índice).
- Mais uso de memória (armazenamento dos ponteiros).

Pseudocódigo de um Nó:
class Node:
    dado
    proximo

Esquema:
[10] -> [20] -> [30] -> None

Exemplo simples de criação em Python:
"""

class Node:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n1.proximo = n2
n2.proximo = n3

# Percorrendo a lista:
atual = n1
while atual:
    print(atual.dado)
    atual = atual.proximo

# --------------------------------------------
# Diferenças entre Arrays e Listas Ligadas
# --------------------------------------------
"""
| Característica       | Arrays                    | Listas Ligadas          |
|----------------------|---------------------------|-------------------------|
| Acesso               | Direto (O(1))             | Sequencial (O(N))       |
| Inserção no meio     | Ineficiente (O(N))        | Rápida (O(1) se tiver o nó) |
| Uso de memória       | Contíguo e compacto       | Mais memória (ponteiros)|
| Redimensionamento    | Difícil (em algumas linguagens) | Fácil               |
"""

# --------------------------------------------
# Filas (Queues)
# --------------------------------------------
"""
Definição:
- Estrutura FIFO (First In, First Out).
- Primeiro a entrar é o primeiro a sair.

Operações básicas:
- Enqueue (inserir no final)
- Dequeue (remover do início)

Exemplo de fila no mundo real:
- Fila de pessoas no caixa do supermercado.

Exemplo em Python:
"""

from collections import deque

fila = deque()
fila.append("Pessoa 1")
fila.append("Pessoa 2")
print("Primeiro a sair:", fila.popleft())

# --------------------------------------------
# Pilhas (Stacks)
# --------------------------------------------
"""
Definição:
- Estrutura LIFO (Last In, First Out).
- Último a entrar é o primeiro a sair.

Operações básicas:
- Push (inserir no topo)
- Pop (remover do topo)

Exemplos de uso:
- Pilha de pratos.
- Navegador web (histórico de páginas).

Exemplo em Python:
"""

pilha = []
pilha.append("Página 1")
pilha.append("Página 2")
print("Último a sair:", pilha.pop())

# --------------------------------------------
# Matrizes (Arrays Multidimensionais)
# --------------------------------------------
"""
Definição:
- Arrays com mais de uma dimensão.
- Exemplo clássico: matriz 2x2, 3x3, etc.

Uso comum:
- Representação de imagens.
- Tabelas de dados.
- Mapas em jogos.

Exemplo de uma matriz 2x3:
[
 [1, 2, 3],
 [4, 5, 6]
]

Pseudocódigo para acessar elemento da segunda linha, terceira coluna:
matriz[1][2]

Exemplo em Python:
"""

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]
print("Elemento na posição (2,3):", matriz[1][2])

# --------------------------------------------
# Exercícios Propostos
# --------------------------------------------
"""
1) Crie um código para implementar uma fila usando apenas listas.

2) Escreva um pseudocódigo para adicionar um elemento no início de uma lista ligada.

3) Explique as vantagens de usar uma pilha em comparação com uma lista simples.

4) Construa uma matriz 3x3 e faça um algoritmo que percorra todos os seus elementos.

5) Pergunta teórica:
Qual estrutura você escolheria para um programa de controle de chamadas telefônicas recebidas (ordem de atendimento) e por quê?

"""

"""
Essa foi a terceira aula!
Na próxima, podemos aprofundar em árvores e outras estruturas mais avançadas.
"""
