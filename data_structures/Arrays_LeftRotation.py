def shift_left(arr, n):
    return arr[n:] + arr[:n]

n = 4
arr = [1,2,3,4,5]
print(shift_left(arr, n))