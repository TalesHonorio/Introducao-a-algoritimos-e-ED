# Análise de Complexidade de Algoritmos - Aula 2

"""
Disciplina: Introdução a Algoritmos e Estruturas de Dados
Tema: Análise de Complexidade de Algoritmos

Nesta aula vamos entender como medir a eficiência de um algoritmo, como expressar essa eficiência e como fazer a análise teórica de desempenho.
"""

# ------------------------------------------------------------
# 1. Eficiência de Algoritmos
# ------------------------------------------------------------
"""
O que significa um algoritmo ser eficiente?
- Menor tempo de execução.
- Menor uso de memória.

Por que medir a eficiência?
- Para escolher o melhor algoritmo entre várias opções.
- Para garantir que o programa funcione bem mesmo com grandes quantidades de dados.
"""

# Exemplo: Comparando dois algoritmos para encontrar o maior número em uma lista

def encontrar_maior_1(lista):
    maior = lista[0]
    for elemento in lista:
        if elemento > maior:
            maior = elemento
    return maior

def encontrar_maior_2(lista):
    return max(lista)

"""
Ambos resolvem o problema, mas podem ter diferenças de desempenho dependendo do tamanho da lista.
"""

# ------------------------------------------------------------
# 2. Análise Empírica
# ------------------------------------------------------------
"""
Analisar empiricamente significa medir o tempo de execução e uso de memória na prática.
Exemplo de ferramentas:
- time (módulo do Python)
- timeit (módulo do Python)

Exemplo de medição de tempo:
"""

import time

inicio = time.time()
resultado = encontrar_maior_1([1, 5, 3, 9, 2, 8])
fim = time.time()

print("Tempo de execução:", fim - inicio, "segundos")

# ------------------------------------------------------------
# 3. Análise Assintótica
# ------------------------------------------------------------
"""
Análise assintótica = Estudo do comportamento do algoritmo quando o tamanho da entrada tende ao infinito (muito grande).

Por que fazer análise assintótica?
- Não depende do computador usado.
- Permite comparar algoritmos teoricamente.
"""

# ------------------------------------------------------------
# 4. Operação Básica do Algoritmo
# ------------------------------------------------------------
"""
Definição:
- A operação que mais influencia o tempo de execução do algoritmo.
- Exemplo: Em um algoritmo de soma de lista, a operação básica é a soma.

Exemplo de contagem:
"""

def soma_lista(lista):
    soma = 0
    for elemento in lista:
        soma += elemento
    return soma

"""
Aqui, a operação básica é a soma dentro do loop.
Se a lista tiver N elementos, teremos N operações de soma.
"""

# ------------------------------------------------------------
# 5. Ordem de Crescimento
# ------------------------------------------------------------
"""
Ordem de crescimento = Como o número de operações cresce conforme a entrada aumenta.

Principais classes de crescimento:

- O(1) -> Constante
- O(log N) -> Logarítmica
- O(N) -> Linear
- O(N log N) -> Linearítmica
- O(N^2) -> Quadrática
- O(2^N) -> Exponencial
- O(N!) -> Fatorial

Exemplos teóricos:
1. O(1): Acesso direto a um elemento de uma lista.
2. O(N): Loop simples que percorre a lista inteira.
3. O(N^2): Dois loops aninhados.

Exemplo de código O(N^2):
"""

def imprimir_pares(lista):
    for i in lista:
        for j in lista:
            print(i, j)

"""
Se a lista tiver N elementos, o número de impressões será N * N = N².
"""

# ------------------------------------------------------------
# 6. Especificação da Entrada do Algoritmo
# ------------------------------------------------------------
"""
Antes de calcular a complexidade, precisamos definir:
- Qual o tamanho da entrada? (Exemplo: número de elementos na lista -> N)
- Qual a operação básica?

Exemplo:
Problema: Somar todos os elementos de uma lista.
Entrada: Lista de N elementos.
Operação básica: Soma.
Complexidade: O(N), porque há N somas.
"""

# ------------------------------------------------------------
# 7. Notações (Big-O, Big Ômega, Big Theta)
# ------------------------------------------------------------
"""
Três principais formas de expressar a complexidade:

1. Big-O (O grande)
- Indica o limite superior do crescimento.
- Representa o pior caso.

2. Big Ômega (Ω)
- Indica o limite inferior.
- Representa o melhor caso.

3. Big Theta (Θ)
- Indica um limite exato.
- Representa quando o melhor e o pior caso têm a mesma ordem.

Exemplo:
Para a busca linear:
- Melhor caso: O(1) (se o elemento estiver logo no início)
- Pior caso: O(N) (se o elemento estiver no final ou não existir)
- Caso médio: Θ(N)
"""

# ------------------------------------------------------------
# 8. Como Obter a Complexidade de um Algoritmo
# ------------------------------------------------------------
"""
Passos:
1. Escolha a operação básica.
2. Conte quantas vezes ela é executada em função da entrada N.
3. Expresse o resultado usando notações assintóticas.

Exemplo:
Problema: Calcular o fatorial de N.

Pseudocódigo:
function fatorial(N):
    resultado = 1
    para i de 1 até N:
        resultado = resultado * i
    retornar resultado

Operação básica: Multiplicação.
Número de operações: N vezes.
Complexidade: O(N).
"""

# ------------------------------------------------------------
# 9. Exercícios Propostos
# ------------------------------------------------------------
"""
1) Analise a complexidade dos seguintes algoritmos:

(a) Algoritmo que percorre uma lista uma vez:
for i in range(N):
    print(i)

(b) Algoritmo com dois loops aninhados:
for i in range(N):
    for j in range(N):
        print(i, j)

(c) Algoritmo com busca binária:
BuscaBinaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    enquanto inicio <= fim:
        meio = (inicio + fim) // 2
        se lista[meio] == alvo:
            retornar True
        se lista[meio] < alvo:
            inicio = meio + 1
        senão:
            fim = meio - 1
    retornar False

2) Pergunta teórica:
Explique com suas palavras a diferença entre Big-O, Big-Ômega e Big-Theta.

3) Extra:
Crie um pequeno algoritmo qualquer e faça a análise de sua complexidade.
"""

"""
Essa foi a segunda aula!
Na próxima, vamos começar a resolver problemas de programação usando as estratégias e análises que aprendemos.
"""
