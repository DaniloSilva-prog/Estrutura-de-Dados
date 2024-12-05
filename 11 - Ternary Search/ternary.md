# A comparação de desempenho entre Ternary Search e Binary Search depende de vários fatores, incluindo o número de comparações, o custo computacional de cada operação e o caso de uso específico.

# Comparação

1) Complexidade Temporal:

    - Binary Search: Reduz a lista em 1/2 a cada iteração, resultando em 𝑂(log⁡2𝑛)

    - Ternary Search: Reduz a lista em 1/3 a cada iteração, resultando em 𝑂(log3𝑛)

* Embora log3𝑛 seja matematicamente menor que log2𝑛 (porque log3𝑛=log2𝑛/log23), o Binary Search realiza menos divisões por iteração, o que o torna geralmente mais eficiente em práticas computacionais.

2) Número de Comparações:

    - No Binary Search, são feitas no máximo 1 comparação por iteração (com o elemento do meio).
    - No Ternary Search, são feitas até 2 comparações por iteração (com os dois pontos médios).

* Isso significa que o Ternary Search pode acabar realizando mais comparações no geral, apesar de reduzir o tamanho da lista de forma um pouco mais agressiva.

3) Custo Computacional por Iteração:

    - O Ternary Search requer calcular dois índices (mid1 e mid2), enquanto o Binary Search calcula apenas um (mid). Este aumento no número de cálculos pode impactar a eficiência.

4) Casos de Uso Específicos:

    - Binary Search é mais eficiente para listas ordenadas devido ao menor número de operações por iteração.
    - Ternary Search pode ser mais adequado para funções unimodais (funções que possuem apenas um pico ou vale), onde o objetivo é localizar o máximo ou mínimo em um intervalo contínuo.

# Resultados Esperados:

- Binary Search geralmente é mais rápido em listas ordenadas, pois tem menos comparações e divisões por iteração.

- Ternary Search tende a ser mais lento devido ao maior custo computacional, mesmo com uma redução mais rápida do intervalo de busca.

# Conclusão:

- Para listas ordenadas, Binary Search é quase sempre superior.

- Ternary Search pode ser vantajoso em casos muito específicos, como buscas em funções unimodais ou contextos onde 𝑂(log3𝑛) é crítico para a aplicação.