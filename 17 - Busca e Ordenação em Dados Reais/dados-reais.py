def bucket_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    
    bucket_count = 10
    bucket_size = (max_val - min_val) / bucket_count

    buckets = [[] for _ in range(bucket_count)]
    
    for num in arr:
        index = int((num - min_val) // bucket_size)
        index = min(index, bucket_count - 1) 
        buckets[index].append(num)
    
    for i in range(bucket_count):
        buckets[i].sort()

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    
    return sorted_arr

def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1
    
    while low <= high and x >= arr[low] and x <= arr[high]:
        pos = low + ((x - arr[low]) * (high - low)) // (arr[high] - arr[low])
        
        if arr[pos] == x:
            return pos
        
        if arr[pos] < x:
            low = pos + 1

        else:
            high = pos - 1
    
    return -1

notas = [92, 85, 71, 99, 63, 74, 56, 88, 100, 60, 45, 73, 82, 68, 91]


notas_ordenadas = bucket_sort(notas)
print("Notas ordenadas:", notas_ordenadas)

nota_procurada = 60
posicao = interpolation_search(notas_ordenadas, nota_procurada)

if posicao != -1:
    print(f"A nota {nota_procurada} foi encontrada na posição {posicao}.")
else:
    print(f"A nota {nota_procurada} não foi encontrada.")
