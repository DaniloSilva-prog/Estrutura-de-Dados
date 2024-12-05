import math

def jump_search(arr, target):

    n = len(arr)

    step = int(math.sqrt(n))
    
    prev = 0
    
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1  
    
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i  
    return "Inexistente na lista" 


if __name__ == "__main__":

    lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 25, 27, 30, 35, 37, 40]
    alvo = 45
    
    indice = jump_search(lista, alvo)
    if indice != -1:
        print(f"Elemento encontrado no índice {indice}.")
    else:
        print("Elemento não encontrado.")
