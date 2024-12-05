# Radix Sort

- O algoritmo Radix Sort pode ser adaptado para trabalhar com diferentes bases. O comportamento do algoritmo depende da base escolhida para representar os números, sendo que a base 10 (decimal) é a mais comum. No entanto, o Radix Sort pode ser modificado para ordenar números em outras bases, como a base 2 (binária).

# Como funciona o Radix Sort com base diferente:

1. Base Decimal (Base 10):
    
    - Na base 10, cada número é representado por 10 dígitos (de 0 a 9). O Radix Sort, nesse caso, ordena os números começando do dígito menos significativo (unidades) até o mais significativo (dígitos de maior valor), utilizando a base 10 em cada iteração.

* Exemplo: 

- Para ordenar números como 170, 45, 75, 90, 802, 24, 2, 66, o algoritmo começa com a unidade (último dígito), depois avança para as dezenas, centenas e assim por diante:

    - Na primeira iteração, ele olha o dígito das unidades (0-9).
    - Na segunda iteração, ele olha o dígito das dezenas (10-99), e assim por diante.


2. Base Binária (Base 2):

    - Para usar a base 2 (binária), o algoritmo pode ser adaptado para operar com números binários em vez de decimais. A diferença aqui é que cada "dígito" é 0 ou 1, e o algoritmo precisa ordenar com base nesses bits, começando pelo bit menos significativo (LSB - Least Significant Bit) até o bit mais significativo (MSB - Most Significant Bit).

* Exemplo: Se quisermos ordenar números binários como 1011, 1100, 0110, e 1001, o Radix Sort começará com o bit mais à direita (unidade binária) e depois vai para o próximo bit à esquerda (dígito binário de valor 2, 4, etc.).

    - Na primeira iteração, ele olha o bit de menor valor (1 ou 0).
    - Na segunda iteração, ele olha o próximo bit, e assim por diante, até o bit mais significativo.

# Adaptação do Radix Sort para Base Binária (Base 2):

- O Radix Sort com base 2 funciona de maneira muito similar ao caso de base 10, mas em vez de ordenar pelos dígitos de 0 a 9, ele ordena os bits de 0 a 1. Cada bit é tratado como um "dígito" e o algoritmo é aplicado da mesma maneira.

* Exemplo prático com base binária:
Vamos considerar os seguintes números binários para ordenar:

- 1011 (11 em decimal)
- 1100 (12 em decimal)
- 0110 (6 em decimal)
- 1001 (9 em decimal)

Primeira iteração (bits menos significativos):

    Olha o bit mais à direita (unidade binária):
    1011, 1100, 0110, 1001 → ordenados como [1100, 1001, 1011, 0110].

Segunda iteração:

    Olha o próximo bit à esquerda:
    1100, 1001, 1011, 0110 → ordenados como [1001, 1100, 1011, 0110].

# Iterações subsequentes:

- Continua olhando para os bits mais à esquerda, repetindo esse processo até que todos os bits tenham sido considerados.

# Modificação para Base 2:

- Ao usar a base binária (base 2), o algoritmo precisa ser alterado para tratar os bits em vez dos dígitos decimais. A mudança seria na forma como os dígitos (ou bits) são extraídos de cada número, além de adaptar a sub-rotina Counting Sort para lidar com dois valores (0 e 1) em vez de 10 (de 0 a 9).

# Resumo:

O Radix Sort pode ser adaptado para qualquer base b, seja base 10 (decimal), base 2 (binária), base 16 (hexadecimal), etc.
Na base 10, cada dígito de 0 a 9 é considerado em cada iteração.

Na base 2, cada número é considerado como uma sequência de bits (0 ou 1), e o algoritmo classifica os números de acordo com cada bit, começando do menos significativo até o mais significativo. Assim, a principal diferença ao usar uma base diferente é a representação dos números e como o algoritmo lê e organiza os "dígitos" de acordo com a base escolhida.