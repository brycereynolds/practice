def bubblesort(vals):

    is_sorted = False
    last_unsorted = len(vals) - 1

    while is_sorted is False:

        is_sorted = True

        for i in range(0, last_unsorted):
            if vals[i] > vals[i + 1]:
                vals[i], vals[i + 1] = vals[i + 1], vals[i]
                is_sorted = False

        last_unsorted -= 1

    return vals

vals = [2,43,234,52,2,312,2,3,321,2,3,23,2,12,3,24,3,3]

print(bubblesort(vals))