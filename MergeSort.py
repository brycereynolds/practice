def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:] + right[j:])
    return result


# I'm not sure if this is valid b/c I am creating a left and right instead
# of doing my sorting in place...
def mergesort(arr):
    if len(arr) < 2: return arr

    middle = int(len(arr) / 2)
    left = mergesort(arr[:middle])
    right = mergesort(arr[middle:])
    return merge(left, right)


arr = [434, 23, 3, 3,2, 1, 4, 5, 6, 4, 3, 2, 1, 85]

print(mergesort(arr))

