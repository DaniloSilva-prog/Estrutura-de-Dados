def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]: 
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
            
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado

def busca_binaria(lista, palavra):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == palavra:
            return True
        elif lista[meio] < palavra:
            inicio = meio + 1
        else:
            fim = meio - 1

    return False 

palavras = ["banana", "sapato", "uva", "aviao", "bicicleta", "carro", "camisa", "zebra", "tigre", "porta"]

ordenadas = merge_sort(palavras)
print("Lista ordenada:", ordenadas)

palavra_procurada = "carro"
if busca_binaria(ordenadas, palavra_procurada):
    print(f"A palavra '{palavra_procurada}' está na lista.")
else:
    print(f"A palavra '{palavra_procurada}' NÃO está na lista.")
