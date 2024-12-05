import random

def quick_sort(arr, pivot_strategy='first'):

    if len(arr) <= 1:
        return arr

    # Escolha do pivô com base na estratégia
    if pivot_strategy == 'first':
        pivot = arr[0]
    elif pivot_strategy == 'last':
        pivot = arr[-1]
    elif pivot_strategy == 'middle':
        pivot = arr[len(arr) // 2]
    elif pivot_strategy == 'median':
        middle = len(arr) // 2
        candidates = [arr[0], arr[-1], arr[middle]]
        pivot = sorted(candidates)[1]  # Mediana de três valores
    else:
        raise ValueError("Estratégia de pivô inválida. Use 'first', 'last', 'middle' ou 'median'.")

    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return quick_sort(less, pivot_strategy) + equal + quick_sort(greater, pivot_strategy)


# Exemplo de uso
if __name__ == "__main__":

    arr_size = 10
    arr = [random.randint(1, 100) for _ in range(arr_size)]  

    print("Ordenação usando o primeiro elemento como pivô:")
    print(quick_sort(arr, pivot_strategy='first'))
    
    print("\nOrdenação usando o último elemento como pivô:")
    print(quick_sort(arr, pivot_strategy='last'))
    
    print("\nOrdenação usando o elemento do meio como pivô:")
    print(quick_sort(arr, pivot_strategy='middle'))
    
    print("\nOrdenação usando a mediana de três como pivô:")
    print(quick_sort(arr, pivot_strategy='median'))
