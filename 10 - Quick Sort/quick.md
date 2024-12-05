# Listas Quase Ordenadas

- Definição: Uma lista é quase ordenada se a maioria dos elementos já está na ordem correta, com poucos elementos fora de lugar.

- Impacto no Quick Sort:

    - Se o primeiro ou o último elemento for escolhido como pivô, o Quick Sort apresentará o pior caso: O(n2 ). Isso ocorre porque a partição tende a gerar subarrays muito desbalanceados (um com n−1 elementos e outro vazio).

    - Escolher o pivô com base na mediana de três ou no elemento do meio melhora o desempenho, já que isso aumenta a chance de subarrays mais balanceados.

# Listas Completamente Desordenadas

- Definição: Uma lista é completamente desordenada quando os elementos estão distribuídos de forma aleatória, sem relação com a ordem correta.

- Impacto no Quick Sort:

    - A escolha do pivô tem menor impacto aqui, pois a probabilidade de dividir a lista de maneira balanceada aumenta com uma distribuição aleatória.
    - Para listas desordenadas, o Quick Sort tende a apresentar um desempenho próximo ao melhor caso 𝑂(𝑛 log 𝑛).

# Conclusão

- Listas Quase Ordenadas:

    Estratégias ingênuas (pivô como primeiro ou último) resultam em baixa eficiência.
    Usar a mediana de três ou o elemento do meio é crucial para evitar o pior caso.

- Listas Completamente Desordenadas:

    Todas as estratégias funcionam razoavelmente bem, mas a mediana de três tende a ser mais robusta.
    Recomenda-se mediana de três para maior estabilidade em diferentes cenários.