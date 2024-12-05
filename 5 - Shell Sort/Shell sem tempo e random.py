def shell_sort_shell(arr):
    
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

def shell_sort_knuth(arr):

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

def shell_sort_hibbard(arr):

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


arr_shell = [9, 8, 7, 6, 5, 4, 3, 2, 1]
arr_knuth = arr_shell.copy()
arr_hibbard = arr_shell.copy()

print("Original:", arr_shell)

shell_sort_shell(arr_shell)
print("Ordenado com sequência de Shell:", arr_shell)

shell_sort_knuth(arr_knuth)
print("Ordenado com sequência de Knuth:", arr_knuth)

shell_sort_hibbard(arr_hibbard)
print("Ordenado com sequência de Hibbard:", arr_hibbard)
