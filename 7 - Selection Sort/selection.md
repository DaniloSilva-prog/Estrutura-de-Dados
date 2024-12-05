# Selection Sort

- O algoritmo Selection Sort funciona repetidamente selecionando o menor elemento (ou maior, dependendo da ordenação) de uma lista não ordenada e colocando-o na posição correta.

- O desempenho do Selection Sort é diretamente relacionado ao número de elementos na lista. Ele é considerado um algoritmo de ordenação simples, mas seu desempenho não é tão eficiente quando comparado a algoritmos mais avançados como o Quick Sort ou Merge Sort. 

# Listas Pequenas

- Desempenho:

    - Muito eficiente devido ao baixo custo computacional com poucas comparações.
    - Geralmente adequado para listas pequenas em cenários simples ou educacionais.

* Exemplo:

    - Lista: n <= 20

# Listas Medias

- Desempenho:

    - Começa a perder eficiência em relação a algoritmos mais avançados, como Quick Sort e Merge Sort.
    - Ainda viável se a lista estiver muito próxima da ordenação (embora não aproveite esta característica como o Insertion Sort).

* Exemplo

    - Lista: 20 < n <= 100

# Listas Grandes

- Desempenho:

    - Ineficiente para listas grandes devido ao aumento exponencial de comparações.
    - Algoritmos mais sofisticados como Merge Sort e Quick Sort em média são consideravelmente mais rápidos.

* Exemplos:

    - Lista: n > 1000

# Portanto, o Selection Sort é melhor aplicado em listas pequenas ou quando a simplicidade é mais importante do que a eficiência.