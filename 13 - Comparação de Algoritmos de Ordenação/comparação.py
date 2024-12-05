import time
import random

def measure_time_and_comparisons(sort_function, arr):
    comparisons = [0] 
    start_time = time.time()
    sorted_arr = sort_function(arr, comparisons)
    end_time = time.time()
    return sorted_arr, end_time - start_time, comparisons[0]

def shell_sort(arr, comparisons):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                comparisons[0] += 1
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

def merge_sort(arr, comparisons):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L, comparisons)
        merge_sort(R, comparisons)

        i = j = k = 0
        while i < len(L) and j < len(R):
            comparisons[0] += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def selection_sort(arr, comparisons):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            comparisons[0] += 1
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def quick_sort(arr, comparisons):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparisons[0] += 1
            if arr[j] < pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_recursive(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_recursive(arr, low, pi - 1)
            quick_sort_recursive(arr, pi + 1, high)

    quick_sort_recursive(arr, 0, len(arr) - 1)
    return arr

def bucket_sort(arr, comparisons):
    if len(arr) == 0:
        return arr
    
    max_value = max(arr)
    size = max_value // len(arr) + 1  
    buckets = [[] for _ in range(len(arr))]
    
    for i in range(len(arr)):
        j = arr[i] // size
        buckets[j].append(arr[i])

    result = []
    for i in range(len(arr)):
        insertion_sort(buckets[i], comparisons)
        result.extend(buckets[i])
    
    return result

def insertion_sort(arr, comparisons):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            comparisons[0] += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def radix_sort(arr, comparisons):
    def counting_sort(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(len(arr)):
            arr[i] = output[i]

    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

arr_size = 100000
arr = [random.randint(1, 1000000) for _ in range(arr_size)]  

algorithms = {
    "Shell Sort": shell_sort,
    "Merge Sort": merge_sort,
    "Selection Sort": selection_sort,
    "Quick Sort": quick_sort,
    "Bucket Sort": bucket_sort,
    "Radix Sort": radix_sort
}

results = []

for name, func in algorithms.items():
    arr_copy = arr.copy()
    sorted_arr, exec_time, comparisons = measure_time_and_comparisons(func, arr_copy)
    results.append((name, exec_time, comparisons))

for result in results:
    print(f"{result[0]} - Tempo de execucao: {result[1]:.6f} segundos, Comparacoes: {result[2]}")