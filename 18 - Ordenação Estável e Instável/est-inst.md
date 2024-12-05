## Algoritmos estáveis

- Bucket Sort
- Merge Sort
- Radix Sort 

## Resumo dos Exemplos

- Merge Sort: A ordem relativa dos elementos iguais é preservada durante a fusão.
- Radix Sort: A estabilidade é garantida, pois a ordenação dos dígitos não altera a ordem dos números com o mesmo valor no dígito atual.
- Bucket Sort: A estabilidade é mantida dentro de cada balde, especialmente se utilizarmos um algoritmo estável (como o Insertion Sort).

Esses exemplos mostram claramente como a estabilidade funciona nesses algoritmos. Eles mantêm a ordem original dos elementos iguais durante o processo de ordenação.

## Importância da estabilidade

- Em situações em que a lista contém dados complexos, como registros de estudantes com notas e idades, e é necessário ordenar por vários critérios (por exemplo, primeiro por nome e depois por idade), a estabilidade garante que a ordem dos elementos já ordenados anteriormente seja preservada.

- Por exemplo, ao ordenar por nome de estudantes e depois por idade, um algoritmo estável manterá a ordem de idade para os estudantes com o mesmo nome, enquanto um algoritmo não estável poderia trocar a ordem de idade entre eles.