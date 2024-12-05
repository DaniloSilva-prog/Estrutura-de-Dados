# O Merge Sort é um algoritmo de ordenação baseado na técnica de "dividir para conquistar" (divide and conquer). 

- Ele funciona dividindo o problema em partes menores até que sejam fáceis de resolver, resolvendo essas partes individualmente e, em seguida, combinando as soluções para formar o resultado final.

# Conceito de "Dividir para Conquistar" no Merge Sort

- Dividir: A lista é dividida em duas partes aproximadamente iguais até que cada sublista tenha apenas um elemento (que, por definição, está ordenado).

- Conquistar: As sublistas são ordenadas individualmente (nesse caso, a ordenação ocorre ao combinar sublistas menores).

- Combinar: As sublistas ordenadas são mescladas em uma única lista ordenada.

# Exemplo

1) Dividir:

A lista [38, 27, 43, 3, 9, 82, 10] é dividida em duas partes: [38, 27, 43] e [3, 9, 82, 10].
Isso continua até que tenhamos sublistas de tamanho 1, como [38], [27], etc.

2) Conquistar:

A cada etapa, duas sublistas menores são combinadas de forma ordenada, como [38] e [27] virando [27, 38].

3) Combinar:

As sublistas ordenadas são combinadas repetidamente até que a lista inteira esteja ordenada.