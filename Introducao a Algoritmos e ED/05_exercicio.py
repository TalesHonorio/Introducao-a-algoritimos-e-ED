'''
Você tem uma rede composta por vários computadores e conexões com fio entre eles. Seu objetivo é otimizar a conectividade da rede usando exatamente K fios adicionais do seu inventário. A meta é maximizar o número de computadores conectados entre si, respeitando essa limitação.

Dois computadores são considerados conectados se estiverem ligados direta ou indiretamente por conexões com fio. É importante observar que o valor de K sempre será menor que o número de redes isoladas (componentes desconexos) na configuração inicial, e pode até ser zero.

Sua tarefa é determinar o tamanho da maior rede que pode ser formada ao conectar essas redes isoladas com até K fios adicionais.

Ideia:

- Cada computador é um nó.
- Cada conexão com fio existente é uma aresta.
'''


