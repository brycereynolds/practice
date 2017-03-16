def bubblesort(vals):
    swaps = 0
    is_sorted = False
    last_unsorted = len(vals) - 1

    while is_sorted is False:

        is_sorted = True

        for i in range(0, last_unsorted):

            if vals[i] > vals[i + 1]:
                swaps += 1
                vals[i], vals[i + 1] = vals[i + 1], vals[i]
                is_sorted = False

        last_unsorted -= 1

    return swaps
# vals = [23,4,34,12,43,453,3,44,5,3,4,34,4,5]
vals = [1,3,1,2,3,4]

print(bubblesort(vals))
