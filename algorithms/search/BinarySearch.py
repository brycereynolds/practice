def binary_search(arr, q):
    return _binary_search(arr, q, 0, len(arr) - 1)

def _binary_search(arr, q, left, right):
    """
    Intuitive search that requires an already ordered list. Basically you open the list
    halfway, compare if your search term is equal, lt, or gt and then repeat your slicing.

    Time and Space Complexities:
        O(log n)
            - # number of times you can divide n by 2 until you get to 1
    Pros:

    Cons:
    """

    if left > right: return False

    index = (left + right) // 2

    if q == arr[index]:
        return True
    elif q < arr[index]:
        return _binary_search(arr, q, left, index - 1)
    else:
        return _binary_search(arr, q, index + 1, right)


def binary_search_iter(arr, q):
    pass

arr = sorted([434, 23, 3, 3,2, 1, 4, 5, 6, 4, 3, 2, 1, 85])
print(binary_search(arr, 0))