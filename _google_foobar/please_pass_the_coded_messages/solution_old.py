from functools import reduce

def answer(arr):
    arr_str = [str(val) for val in sorted(arr, reverse=True)]
    i = len(arr_str)
    solution = False
    while i > 0:
        for val in permutations(arr_str, i):
            num = int(''.join([v for v in val]))
            b2_list = [int(x) for x in format(num, 'b')]

            if divisible_by_three(b2_list) is True:
                solution = num
                break

        if solution is not False: break
        i -= 1
    return solution

# A binary number is a multiple of 3 if and only if the alternating sum of its bits
# is also a multiple of 3:
def divisible_by_three(iterator):
    multiplier = 1
    accumulator = 0

    for bit in iterator:
        accumulator = (accumulator + bit * multiplier) % 3
        multiplier = 3 - multiplier

    return accumulator == 0

# From https://docs.python.org/2/library/itertools.html#itertools.permutations
def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

# l = [3, 1, 4, 1]
# l = [3, 1, 4, 1, 5, 9]
# print(answer(l))
