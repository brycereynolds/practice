def mergesort(arr, start, end):
    if start >= end: return

    mid = (start + end) // 2
    mergesort(arr, start, mid)
    mergesort(arr, mid + 1, end)
    merge(arr, start, mid, end)

def merge(arr, left_start, left_end, right_end):
    right_start = left_end + 1
    left = left_start
    right = right_start
    result = []

    while left <= left_end and right <= right_end:
        if arr[left] <= arr[right]:
            result += [arr[left]]
            left += 1
        else:
            result += [arr[right]]
            right += 1

    result.extend(arr[left:left_end + 1] + arr[right:right_end + 1])
    arr[left_start:right_end + 1] = result

arr = [434, 23, 3, 3,2, 1, 4, 5, 6, 4, 3, 2, 1, 85]

mergesort(arr, 0, len(arr) - 1)
print(arr)
