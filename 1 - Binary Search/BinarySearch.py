def binary_search(array, target):

    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return "inexistente nesse lista"

# Testando a função
lista = [1, 3, 5, 7, 9, 11]
elemento = 2
indice = binary_search(lista, elemento)

print(f"O índice do elemento {elemento} é {indice}.")
