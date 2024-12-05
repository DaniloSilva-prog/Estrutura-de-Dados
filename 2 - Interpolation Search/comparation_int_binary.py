def interpolation_search(arr, x):

    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= x <= arr[high]:

        pos = low + ((x - arr[low]) * (high - low) // (arr[high] - arr[low]))


        if arr[pos] == x:
            return pos

        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return "Inexistente"


def binary_search(arr, x):

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return "Inexistente"



def test_search_algorithms():

    uniform_list = list(range(0, 10001, 10)) 

    non_uniform_list = [i ** 2 for i in range(300)] 


    target = 3400

    print("Uniform List:")
    print("Interpolation Search Index:", interpolation_search(uniform_list, target))
    print("Binary Search Index:", binary_search(uniform_list, target))

    print("\nNon-uniform List:")
    print("Interpolation Search Index:", interpolation_search(non_uniform_list, target))
    print("Binary Search Index:", binary_search(non_uniform_list, target))

test_search_algorithms()
