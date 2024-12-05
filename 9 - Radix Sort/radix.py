import random

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n 
    count = [0] * 10 

    for num in arr:
        index = (num // exp) % 10
        count[index] += 1
        
    for i in range(1, 10):
        count[i] += count[i - 1]


    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):

    max_num = max(arr)
    exp = 1 

    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


if __name__ == "__main__":
    
    arr_size = 10
    arr_2digitos = [random.randint(10, 99) for _ in range(arr_size)] 
    arr_5digitos = [random.randint(10000, 99999) for _ in range(arr_size)]
    arr_10digitos = [random.randint(1000000000, 9999999999) for _ in range(arr_size)]  
    
    print("\nLista original:", arr_2digitos)
    radix_sort(arr_2digitos)
    print("Lista ordenada:", arr_2digitos)
    
    print("\nLista original:", arr_5digitos)
    radix_sort(arr_5digitos)
    print("Lista ordenada:", arr_5digitos)

    print("\nLista original:", arr_10digitos)
    radix_sort(arr_10digitos)
    print("Lista ordenada:", arr_10digitos)

