# O Binary Search depende de dividir a lista repetidamente em duas metades e descartar a metade que não pode conter o elemento procurado. Para que essa abordagem funcione, a lista deve estar ordenada.

# Comparação no Meio: 
- O algoritmo compara o elemento-alvo com o elemento no meio da lista. Se a lista estiver ordenada, podemos determinar de forma confiável se o alvo está na metade esquerda (menores que o meio) ou na metade direita (maiores que o meio).

# Eliminação de Metades: 
- Em uma lista desordenada, não é possível garantir que os elementos em uma metade sejam todos menores ou maiores que o elemento no meio. Isso quebraria a lógica do algoritmo.

# Exemplo:

- Lista Ordenada

lista_ordenada = [2, 4, 6, 8, 10]
print(binary_search(lista_ordenada, 8))  # Saída: 3

- Lista desordenada

lista_desordenada = [8, 2, 10, 4, 6]
print(binary_search(lista_desordenada, 8))  # Saída: -1 - Saida Falsa

