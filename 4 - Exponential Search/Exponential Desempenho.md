# O Exponential Search é uma combinação do Jump Search e da Busca Binária:

- Jump Search fornece a estratégia de explorar rapidamente a lista com "saltos" exponenciais, diminuindo o tamanho do intervalo de busca.
- Busca Binária é usada para refinar a busca dentro do intervalo encontrado pelo salto exponencial, fazendo a busca ser eficiente mesmo para listas grandes.

Isso torna o Exponential Search especialmente útil em listas grandes, onde o uso de busca binária após encontrar um intervalo pode melhorar o tempo de busca.

# Trazendo um bom desempenho em listas pequenas por causa do Jump Search, e um bom desempenho em listas grandes por causa do Binary Search