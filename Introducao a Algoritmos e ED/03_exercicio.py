'''
Problema: Atendimento em uma Central de Suporte Técnico

- Contexto:
Uma empresa de tecnologia oferece um serviço de suporte técnico por telefone. Os clientes ligam quando precisam de ajuda e as chamadas são atendidas por ordem de chegada.

- Requisitos principais do sistema:
** As chamadas devem ser atendidas na ordem em que chegam (primeiro a ligar = primeiro a ser atendido → comportamento FIFO).
** Novas ligações devem ser adicionadas ao final da fila.
** Quando um atendente estiver disponível, a próxima ligação da fila deve ser atendida.

- Solução usando Fila:
Para garantir a ordem de atendimento, o sistema de gerenciamento de chamadas implementa uma fila, onde:

** Cada cliente que liga é representado por um elemento da fila.
** A operação de enqueue ocorre quando o cliente liga (adicionar no final da fila).
** A operação de dequeue ocorre quando um atendente inicia o atendimento (remover do início da fila).

'''