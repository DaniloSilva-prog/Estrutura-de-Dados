def binary_search(livros, isbn_desejado):

    inicio = 0
    fim = len(livros) - 1
    
    while inicio <= fim:

        meio = (inicio + fim) // 2
        livro = livros[meio]
        

        if livro['ISBN'] == isbn_desejado:
            return livro  
        elif livro['ISBN'] < isbn_desejado:

            inicio = meio + 1
        else:
 
            fim = meio - 1
    
    return None

livros = [
    {'ISBN': '0001', 'titulo': 'Livro A', 'autor': 'Autor A'},
    {'ISBN': '0003', 'titulo': 'Livro C', 'autor': 'Autor C'},
    {'ISBN': '0005', 'titulo': 'Livro E', 'autor': 'Autor E'},
    {'ISBN': '0007', 'titulo': 'Livro G', 'autor': 'Autor G'},
    {'ISBN': '0010', 'titulo': 'Livro J', 'autor': 'Autor J'},
    {'ISBN': '0015', 'titulo': 'Livro K', 'autor': 'Autor K'},
    {'ISBN': '0022', 'titulo': 'Livro O', 'autor': 'Autor O'},
    {'ISBN': '0035', 'titulo': 'Livro P', 'autor': 'Autor P'},
]

# Testando a função de busca binária
isbn_procurado = '0010'
livro_encontrado = binary_search(livros, isbn_procurado)

if livro_encontrado:
    print(f'Livro encontrado: {livro_encontrado}')
else:
    print('Livro não encontrado.')
