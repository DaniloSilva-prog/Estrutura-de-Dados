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



def test_search_algorithms():

    uniform_list = list(range(0, 10001, 10)) 
    no_uniform_list = [i ** 2 for i in range(300)] 

    target = 3500

    print("Uniform List:")
    print("Interpolation Search Index:", interpolation_search(uniform_list, target))


    print("\nNo-uniform List:")
    print("Interpolation Search Index:", interpolation_search(no_uniform_list, target))

test_search_algorithms()
