arr = [4, 12, 3, 66, 55, 78, 79, 6, 7, 4, 3, 2, 100]

def sort(arr, left, right):
    if(left >= right): return

    midway = partition(arr, left, right)

    sort(arr, left, midway - 1)
    sort(arr, midway, right)
    return arr

def partition(arr, left, right):
    pivot = arr[left]
    while left <= right:
        while arr[left] < pivot: left += 1
        while arr[right] > pivot: right -= 1

        if left <= right: 
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return left


print(sort(arr, 0, len(arr) - 1))
