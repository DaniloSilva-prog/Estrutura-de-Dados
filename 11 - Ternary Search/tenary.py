def ternary_search(arr, target):

    left, right = 0, len(arr) - 1
    
    while left <= right:

        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        if target < arr[mid1]:
            right = mid1 - 1 
        elif target > arr[mid2]:
            left = mid2 + 1 
        else:
            left = mid1 + 1 
            right = mid2 - 1
    
    return -1

if __name__ == "__main__":
    lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 25, 30, 46, 57, 68, 80]
    elemento = 25
    resultado = ternary_search(lista, elemento)
    if resultado != -1:
        print(f"Elemento encontrado no índice: {resultado}")
    else:
        print("Elemento não encontrado.")
