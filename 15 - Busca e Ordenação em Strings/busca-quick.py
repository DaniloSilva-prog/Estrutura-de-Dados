def quick_sort(arr, pivot_strategy='first'):
    if len(arr) <= 1:
        return arr

    if pivot_strategy == 'first':
        pivot = arr[0]
    elif pivot_strategy == 'last':
        pivot = arr[-1]
    elif pivot_strategy == 'middle':
        pivot = arr[len(arr) // 2]
    elif pivot_strategy == 'median':
        middle = len(arr) // 2
        candidates = [arr[0], arr[-1], arr[middle]]
        pivot = sorted(candidates)[1] 
    else:
        raise ValueError("Estratégia de pivô inválida. Use 'first', 'last', 'middle' ou 'median'.")

    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return quick_sort(less, pivot_strategy) + equal + quick_sort(greater, pivot_strategy)

def binary_search(arr, word):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == word:
            return True 
        elif arr[mid] < word:
            left = mid + 1
        else:
            right = mid - 1

    return False  

if __name__ == "__main__":

    palavras = ["banana", "sapato", "uva", "aviao", "bicicleta", "carro", "camisa", "zebra", "tigre", "porta"]

    palavras_ordenadas = quick_sort(palavras, pivot_strategy='middle')
    print("Lista de palavras ordenadas:", palavras_ordenadas)
    palavras_ordenadas = quick_sort(palavras, pivot_strategy='first')
    print("Lista de palavras ordenadas:", palavras_ordenadas)
    palavras_ordenadas = quick_sort(palavras, pivot_strategy='last')
    print("Lista de palavras ordenadas:", palavras_ordenadas)
    palavras_ordenadas = quick_sort(palavras, pivot_strategy='median')
    print("Lista de palavras ordenadas:", palavras_ordenadas)
    
    palavra_procurada = "carro"
    if binary_search(palavras_ordenadas, palavra_procurada):
        print(f"\nA palavra '{palavra_procurada}' está na lista.")
    else:
        print(f"\nA palavra '{palavra_procurada}' NÃO está na lista.")
