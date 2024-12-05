def binary_search(arr, left, right, x):

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1  

def exponential_search(arr, x):

    if arr[0] == x:
        return 0

    i = 1
    while i < len(arr) and arr[i] <= x:
        i *= 2

    return binary_search(arr, i // 2, min(i, len(arr) - 1), x)

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 30, 35, 40, 45, 50, 60, 70]
x = 25
result = exponential_search(arr, x)

if result != -1:
    print(f"Elemento encontrado na posição {result}")
else:
    print("Elemento não encontrado")
