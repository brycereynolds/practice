from math import sqrt

def mergesort(arr):
    for j in range(1, len(arr)):
        j *= 2
        for i in range(0, len(arr), j):
            increment = j if i + j < len(arr) else len(arr) - (i + 1)

            start = i
            mid = (i + (increment // 2)) - 1
            end = (i + increment) - 1

            print("start: {0} mid:{1} end:{2}".format(start,mid,end))
            merge(arr, i, mid, end)
    merge(arr, 0, len(arr) // 2, len(arr) - 1)
    return arr

# [1, 2, 3, 3, 2, 3, 4, 4, 23, 434, 5, 6, 2, 1, 1, 85]

def merge(arr, left_start, right_start, right_end):
    left_end = right_start - 1
    left = left_start
    right = right_start
    result = []

    while left <= left_end and right <= right_end:
        if arr[left] <= arr[right]:
            result += [arr[left]]
            left += 1
        else:
            result += [arr[right]]
            # self.swaps += (left_end + 1) - left
            right += 1

    result.extend(arr[left:left_end + 1] + arr[right:right_end + 1])
    arr[left_start:right_end + 1] = result

arr = [434, 23, 3, 3,2, 1, 4, 5, 6, 4, 3, 2, 1, 85]
print(mergesort(arr))
