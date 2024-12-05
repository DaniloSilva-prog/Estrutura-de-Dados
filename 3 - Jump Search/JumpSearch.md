# Comparando tempo entre os dois

- Jump Search é mais lento em todos os tamanhos de lista devido ao comportamento 𝑂(raiz(n)), enquanto o Binary Search tem complexidade 𝑂(log 𝑛 ). À medida que o tamanho da lista aumenta, a diferença de desempenho entre os dois algoritmos se torna mais significativa.

- Em aplicações práticas, o Binary Search é preferido em listas ordenadas por ser mais eficiente. No entanto, o Jump Search pode ser útil em situações específicas, como quando os dados estão armazenados em estruturas com acesso sequencial (ex.: sistemas de arquivos ou bancos de dados).

# Listas Pequenas 

- Em relação a listas pequenas a comparação fica praticamente com um intervalo bem pequeno, com uma agilidade um pouco melhor para o Binary Search.

# Listas Grandes

- Conforme for aumentando o tamanho da lista a discrêpancia de tempo entre os dois só aumenta, enquanto o JumpSearch aumenta em questão de um numero elevado, o Binary Search se mantem estavel em um tempo adequado.

