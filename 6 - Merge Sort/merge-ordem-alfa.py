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

palavras = ["banana", "sapato", "uva", "aviao", "bicicleta", "carro", "camisa", "zebra", "tigre", "porta"]
ordenadas = merge_sort(palavras)
print("Lista ordenada:", ordenadas)