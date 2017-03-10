arr = [4, 12, 3, 66, 55, 78, 79, 6, 7, 4, 3, 2, 100]

def sort(arr):
    is_sorted = False
    last_unsorted = len(arr) - 1
    while is_sorted is False:

        is_sorted = True

        for i in range(0, last_unsorted):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

        last_unsorted -= 1

    return arr

print(sort(arr))

