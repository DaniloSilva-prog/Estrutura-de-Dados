def bucket_sort(arr):
    n = len(arr)
    
    buckets = [[] for _ in range(n)]
    
    for num in arr:
        index = int(num * n)  
        buckets[index].append(num)
    
    for i in range(n):
        buckets[i].sort()
    
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)
    
    return sorted_array

if __name__ == "__main__":
    
    arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    print("Array original:", arr)
    sorted_arr = bucket_sort(arr)
    print("Array ordenado:", sorted_arr)
