import cProfile, pstats

SENTINEL = 10**8

def mergesort(vals):
    if len(vals) < 2: return vals

    mid = int(len(vals) / 2)
    left = mergesort(vals[:mid])
    right = mergesort(vals[mid:])

    return merge(left, right)

def merge(_left, _right):
    global swaps
    left = _left + [SENTINEL]
    right = _right + [SENTINEL]
    i, j = 0, 0
    result = []
    for _ in range(len(_left) + len(_right)):
    # while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            # result.append(left[i])
            result += [left[i]]
            i += 1
        else:
            # result.append(right[j])
            result += [right[j]]
            swaps += len(left) - i
            j += 1

    # result.extend(left[i:] + right[j:])
    return result

def count_inversions(arr):
    global swaps
    swaps = 0
    mergesort(arr)
    return swaps

####### BELOW THIS LINE IS NOT SUBMITTED


# fname = 'MergeSortCountSwaps_input00.txt'
fname = 'MergeSortCountSwaps_input11.txt'
with open(fname) as f:
    content = f.readlines()

pr = cProfile.Profile()
pr.enable()

for i in range(1, len(content), 2):
    n = int(content[i].strip())
    arr = list(map(int, content[i + 1].strip().split(' ')))

    pr = cProfile.Profile()
    pr.enable()
    print(count_inversions(arr))
    pr.disable()
    ps = pstats.Stats(pr).sort_stats('tottime')
    ps.print_stats()



