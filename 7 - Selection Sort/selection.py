import random

def selection_sort(arr):
    n = len(arr)
    for i in range(n):

        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        print(f"Iteração {i + 1}: {arr}")

arr_size = 10
arr = [random.randint(1, 100) for _ in range(arr_size)]  

print("Lista inicial:", arr)
print("\nProcesso de ordenação:")
selection_sort(arr)
print("\nLista ordenada:", arr)
