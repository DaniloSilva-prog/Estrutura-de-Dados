- O Exponential Search combina elementos de dois algoritmos de busca eficientes: Jump Search e Binary Search. Vamos detalhar como cada um desses algoritmos contribui para a solução do problema de encontrar um elemento em uma lista ordenada.

# Jump Search

- O Jump Search é um algoritmo que divide a lista em blocos de tamanho fixo e "salta" entre os blocos, procurando pelo elemento dentro de um intervalo.

1) Dividimos a lista em blocos de tamanho √n (onde n é o tamanho da lista).
2) Saltamos de bloco em bloco até encontrar um bloco que contém o elemento procurado ou ultrapassá-lo.
3) Em seguida, realizamos uma busca linear dentro do bloco para localizar o elemento.

- No Exponential Search, a ideia de "salto" é usada de forma análoga, mas de maneira exponencial. Em vez de saltar de bloco em bloco com um tamanho fixo (como no Jump Search), o algoritmo começa a saltar de forma exponencial (i.e., dobrando a distância a cada iteração) até encontrar um intervalo onde o elemento procurado pode estar.

# Binary Search 

1) Começamos com o intervalo completo da lista e calculamos o índice do meio.

2) Comparamos o valor do elemento no meio com o valor procurado:
    - Se for o valor procurado, encontramos o elemento.
    - Se o valor procurado for menor, ajustamos o intervalo para a metade inferior.
    - Se o valor procurado for maior, ajustamos o intervalo para a metade superior.

3) Continuamos esse processo de "divisão ao meio" até encontrar o elemento ou determinar que ele não está na lista.

- No Exponential Search, depois de encontrar o intervalo possível usando a busca exponencial, o algoritmo usa a busca binária para procurar o elemento dentro desse intervalo. Isso faz com que o Exponential Search combine a vantagem de reduzir rapidamente a área de busca (usando saltos exponenciais) e, em seguida, realizar a busca de forma eficiente dentro do intervalo encontrado (usando a busca 
binária).

# Exponential Search

1) Primeiro, "salta" exponencialmente (como no Jump Search): O algoritmo começa com um índice i = 1 e dobra i a cada iteração (i.e., i = 1, 2, 4, 8, 16, ...) até encontrar um valor maior ou igual ao elemento procurado ou ultrapassar o fim da lista.

    - Este processo é semelhante ao Jump Search porque, assim como o Jump Search, o Exponential Search aumenta rapidamente o intervalo de busca.

    - A principal diferença é que no Exponential Search, o "salto" não tem um tamanho fixo, mas dobra a cada iteração, o que acelera a descoberta do intervalo onde o valor pode estar.

2) Depois, aplica a Busca Binária (como no Binary Search): Uma vez encontrado o intervalo onde o valor procurado pode estar (entre i // 2 e i), o algoritmo usa Busca Binária nesse intervalo para localizar o elemento.

    - A busca binária é eficiente porque, após o salto exponencial, o intervalo onde o valor pode estar é significativamente reduzido, tornando a busca binária extremamente eficiente.
