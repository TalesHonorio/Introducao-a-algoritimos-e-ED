# Estruturas de Dados - Aula 4

"""
Disciplina: Introdução a Algoritmos e Estruturas de Dados
Tema: Árvores

Conteúdo:
- Definições básicas
- Árvore Binária
- Percursos em Árvores Binárias (Pre-order, In-order, Pos-order)
- Heap
"""

# --------------------------------------------
# Definições Básicas
# --------------------------------------------
"""
O que é uma árvore?
- Estrutura de dados hierárquica com um elemento raiz (root) e subelementos (filhos).
- Cada nó pode ter 0 ou mais filhos.

Termos importantes:
- Raiz (Root): o nó principal
- Folha (Leaf): nó sem filhos
- Grau de um nó: número de filhos
- Altura da árvore: maior distância da raiz até uma folha

Aplicações:
- Sistemas de arquivos
- Organização de hierarquias
- Árvores de decisão
- Compiladores (árvores de sintaxe)
"""

# --------------------------------------------
# Árvore Binária
# --------------------------------------------
"""
Definição:
- Cada nó possui no máximo dois filhos: esquerdo e direito.

Representação de um nó:
class No:
    valor
    esquerda
    direita

Exemplo (visual):
        10
       /  \
      5    15
     / \     \
    3   7     18

Exemplo em Python:
"""

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

# Criando a árvore acima
raiz = No(10)
raiz.esquerda = No(5)
raiz.direita = No(15)
raiz.esquerda.esquerda = No(3)
raiz.esquerda.direita = No(7)
raiz.direita.direita = No(18)

# --------------------------------------------
# Percursos em Árvores Binárias
# --------------------------------------------
"""
1. Pre-order (Pré-Ordem): visita o nó -> esquerda -> direita
2. In-order (Em-Ordem): visita esquerda -> nó -> direita
3. Post-order (Pós-Ordem): visita esquerda -> direita -> nó

Aplicações:
- In-order: usado para exibir BSTs em ordem crescente
- Pre-order: usado para copiar a árvore
- Post-order: usado para excluir a árvore (liberar memória)
"""

# Percursos implementados

def pre_order(no):
    if no:
        print(no.valor, end=' ')
        pre_order(no.esquerda)
        pre_order(no.direita)

def in_order(no):
    if no:
        in_order(no.esquerda)
        print(no.valor, end=' ')
        in_order(no.direita)

def post_order(no):
    if no:
        post_order(no.esquerda)
        post_order(no.direita)
        print(no.valor, end=' ')

print("Percurso In-order:")
in_order(raiz)
print("\nPercurso Pre-order:")
pre_order(raiz)
print("\nPercurso Post-order:")
post_order(raiz)

# --------------------------------------------
# Exemplos com bibliotecas
# --------------------------------------------

"""
Usando a biblioteca `binarytree` para criar e visualizar árvores binárias.
"""

from binarytree import Node as BTNode

root_bt = BTNode(10)
root_bt.left = BTNode(5)
root_bt.right = BTNode(15)
root_bt.left.left = BTNode(3)
root_bt.left.right = BTNode(7)
root_bt.right.right = BTNode(18)

print("\nVisualização da árvore com binarytree:")
print(root_bt)

"""
Usando a biblioteca `bintrees` para criar uma AVL Tree com chaves personalizadas.
"""

from bintrees import AVLTree

class Usuario:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __repr__(self):
        return f"Usuario(id={self.id}, nome='{self.nome}')"

usuarios = [
    Usuario(10, "Ana"),
    Usuario(5, "Bruno"),
    Usuario(15, "Clara"),
    Usuario(3, "Daniel"),
    Usuario(7, "Eva")
]

arvore_avl = AVLTree()
for u in usuarios:
    arvore_avl.insert(u.id, u)

print("\nPercurso In-Order (AVLTree com bintrees):")
for chave, usuario in arvore_avl.items():
    print(chave, "->", usuario)

# --------------------------------------------
# Heap
# --------------------------------------------
"""
Definição:
- Estrutura de árvore binária completa usada para implementar filas de prioridade.
- Dois tipos principais:
    - Min-Heap: o menor valor está na raiz
    - Max-Heap: o maior valor está na raiz

Propriedades:
- Árvore completa (todos os níveis cheios, exceto talvez o último)
- Representada comumente por vetores (arrays)

Aplicações:
- Algoritmos de ordenação (HeapSort)
- Gerenciamento de tarefas (prioridade)
- Algoritmos de caminho mínimo (Dijkstra)

Exemplo de Max-Heap:
        20
       /  \
     18    10
    /  \
   8    5

Pseudocódigo para inserir em Max-Heap:
1. Adiciona o novo elemento no final do array
2. Sobe o elemento (heapify-up) até manter a propriedade de heap
"""

import heapq

# Min-Heap em Python (com heapq)
valores = [20, 5, 15, 30, 10]
heapq.heapify(valores)
print("Min-Heap criado:", valores)

heapq.heappush(valores, 3)
print("Após inserção de 3:", valores)

menor = heapq.heappop(valores)
print("Menor elemento removido:", menor)

# --------------------------------------------
# Exercícios Propostos
# --------------------------------------------
"""
1) Construa manualmente uma árvore binária com os seguintes valores: 12, 6, 14, 3, 8
   a) Escreva o percurso in-order dessa árvore.

2) Implemente uma função que conte quantas folhas existem em uma árvore binária.

3) Dado um array [40, 30, 20, 10], transforme-o em um Min-Heap e exiba o resultado.

4) Explique com suas palavras qual a diferença entre árvore binária e heap.

5) Desenhe a árvore abaixo e diga o resultado do percurso pós-ordem:
       9
      / \
     4   11
    / \    \
   2   7   15
"""

"""
Na próxima aula, podemos estudar Grafos!
"""
