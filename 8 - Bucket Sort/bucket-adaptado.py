import random

def bucket_sort_integers(arr):
    if not arr:
        return []
    
    min_val, max_val = min(arr), max(arr)
    
    num_buckets = len(arr)
    bucket_range = (max_val - min_val + 1) / num_buckets
    
    buckets = [[] for _ in range(num_buckets)]
    
    for num in arr:
        index = int((num - min_val) // bucket_range)

        if index == num_buckets:  
            index -= 1
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()
    
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)
    
    return sorted_array

if __name__ == "__main__":
    arr_size = 10
    arr = [random.randint(1, 100) for _ in range(arr_size)]  
    
    print("Array original:", arr)
    sorted_arr = bucket_sort_integers(arr)
    print("Array ordenado:", sorted_arr)
