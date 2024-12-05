# No algoritmo Bucket Sort, os baldes desempenham o papel de categorias intermediárias para agrupar os elementos antes de serem ordenados. 

1) Criação dos Baldes:

    - O número de baldes é geralmente escolhido como igual ao número de elementos na lista de entrada, mas isso pode variar dependendo do caso.
    - Cada balde é representado como uma lista vazia.

2) Distribuição dos Elementos:

    - Cada número é mapeado para um balde com base na fórmula: 
        indice = [numero x n]
    onde n é numero de baldes.

    - Essa fórmula usa a propriedade dos números em ponto flutuante no intervalo (0, 1), o valor de (numero x n) sera um indice valido de balde

# Ordenação dos Baldes

1) Ordenação Individual:

    - Cada balde é ordenado separadamente usando um algoritmo de ordenação.
    - Como os baldes contêm apenas uma fração dos elementos totais, a ordenação de cada balde é eficiente.

# Concatenando os Baldes

- Após ordenar os baldes, todos os elementos são concatenados na ordem dos índices dos baldes.

# Resumo do Processo

- Preenchimento: Cada número vai para um balde com base em sua posição relativa no intervalo [0,1).
- Ordenação: Os elementos dentro de cada balde são ordenados.
- Concatenar: Todos os baldes são unidos em sequência para formar a lista ordenada.
