# Estruturas de Dados - Aula 6

"""
Disciplina: Introdução a Algoritmos e Estruturas de Dados
Tema: Algoritmos de Ordenação e Busca

Conteúdo:
- Definições
- Lista de algoritmos de ordenação
- Bubble Sort
- Merge Sort
- Quick Sort
- Busca Linear
- Busca Binária
- Exercícios
"""

# --------------------------------------------
# Definições
# --------------------------------------------
"""
Ordenação é o processo de reorganizar os elementos de uma estrutura de dados em uma ordem específica, geralmente crescente ou decrescente.

Objetivos:
- Facilitar busca binária
- Organização e legibilidade
- Preparação para algoritmos mais eficientes

Critérios importantes:
- Estabilidade: mantém a ordem relativa de elementos iguais?
- Complexidade de tempo: em média, pior e melhor caso
- Complexidade de espaço: requer espaço adicional?
"""

# --------------------------------------------
# Algoritmos de Ordenação mais comuns
# --------------------------------------------
"""
1. Bubble Sort
2. Selection Sort
3. Insertion Sort
4. Merge Sort
5. Quick Sort
6. Heap Sort
7. Counting Sort (para inteiros)
8. Radix Sort
"""

# --------------------------------------------
# Bubble Sort
# --------------------------------------------
"""
Teoria:
- Percorre o array diversas vezes
- Compara pares adjacentes e troca se estiverem fora de ordem
- Após cada iteração, o maior elemento "borbulha" para o fim

Complexidade:
- Melhor caso: O(n) [quando já está ordenado]
- Médio e pior caso: O(n²)
- Espaço: O(1) - in-place
- Estável: Sim

Exemplo:
Lista original: [4, 2, 5, 1]
Iterações:
[2, 4, 5, 1]
[2, 4, 1, 5]
[2, 1, 4, 5]
[1, 2, 4, 5]
"""

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

print("Bubble Sort:", bubble_sort([4, 2, 5, 1]))

# --------------------------------------------
# Merge Sort
# --------------------------------------------
"""
Teoria:
- Estratégia divide and conquer
- Divide a lista em duas partes, ordena cada uma e mescla

Complexidade:
- Melhor, médio e pior caso: O(n log n)
- Espaço: O(n) [requere cópias]
- Estável: Sim

Exemplo:
[4, 2, 5, 1] → [4, 2] e [5, 1] → [2, 4] e [1, 5] → [1, 2, 4, 5]
"""

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
    return merge(esquerda, direita)

def merge(esq, dir):
    resultado = []
    i = j = 0
    while i < len(esq) and j < len(dir):
        if esq[i] <= dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1
    resultado.extend(esq[i:])
    resultado.extend(dir[j:])
    return resultado

print("Merge Sort:", merge_sort([4, 2, 5, 1]))

# --------------------------------------------
# Quick Sort
# --------------------------------------------
"""
Teoria:
- Estratégia divide and conquer
- Escolhe um pivô, separa menores e maiores, e aplica recursão

Complexidade:
- Melhor e médio caso: O(n log n)
- Pior caso: O(n²) [quando pivô mal escolhido]
- Espaço: O(log n) [pilha da recursão]
- Estável: Não

Exemplo (pivô = 4):
[4, 2, 5, 1] → menores: [2, 1], pivô: 4, maiores: [5] → [1, 2, 4, 5]
"""

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivô = lista[0]
    menores = [x for x in lista[1:] if x <= pivô]
    maiores = [x for x in lista[1:] if x > pivô]
    return quick_sort(menores) + [pivô] + quick_sort(maiores)

print("Quick Sort:", quick_sort([4, 2, 5, 1]))

# --------------------------------------------
# Busca Linear
# --------------------------------------------
"""
- Percorre a lista de forma sequencial
- Simples, mas ineficiente para listas grandes

Complexidade:
- Melhor caso: O(1)
- Pior caso: O(n)
"""

def busca_linear(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

# --------------------------------------------
# Busca Binária
# --------------------------------------------
"""
- Requer lista ordenada
- Divide a lista ao meio, reduz o espaço de busca pela metade

Complexidade:
- O(log n)
"""

def busca_binaria(lista, valor):
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

# --------------------------------------------
# Exercícios Propostos
# --------------------------------------------
"""
1) Execute o Bubble Sort passo a passo com a lista [7, 4, 5, 2, 9]
2) Aplique o Merge Sort em [8, 3, 1, 7, 0, 10, 2]
3) Qual a principal vantagem do Merge Sort sobre o Bubble Sort?
4) O Quick Sort é estável? Justifique.
5) Dado o array [3, 8, 10, 15, 20], aplique busca binária para encontrar 10
6) Qual algoritmo seria melhor para ordenar uma lista quase ordenada? Justifique.
"""
