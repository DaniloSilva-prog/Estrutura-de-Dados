import time
import random

def shell(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def knuth(arr):
    n = len(arr)
    gap = 1
    while gap < n // 3:
        gap = 3 * gap + 1
    while gap >= 1:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 3

def hibbard(arr):
    n = len(arr)
    gap = 1
    while gap <= n // 3:
        gap = 2 * gap + 1
    while gap >= 1:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = (gap - 1) // 2

def tempo(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

def compare_sort_algorithms():
    arr_size = 10 
    arr = [random.randint(1, 100) for _ in range(arr_size)]  
    
    arr_shell = arr.copy()
    arr_knuth = arr.copy()
    arr_hibbard = arr.copy()
    
    time_shell = tempo(shell, arr_shell)
    time_knuth = tempo(knuth, arr_knuth)
    time_hibbard = tempo(hibbard, arr_hibbard)
    
    print(f"Tempo de execução - Shell: {time_shell:.6f} segundos")
    print(f"Tempo de execução - Knuth: {time_knuth:.6f} segundos")
    print(f"Tempo de execução - Hibbard: {time_hibbard:.6f} segundos\n")
    
    print(f"Esse sera a lista original: {arr}\n")
    print(f"Esse sera a lista ordenada shell: {arr_shell}")
    print(f"Esse sera a lista ordenada knuth: {arr_knuth}")
    print(f"Esse sera a lista ordenada hibbard: {arr_hibbard}")
    

compare_sort_algorithms()
