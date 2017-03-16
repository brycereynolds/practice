from itertools import permutations

def answer(arr):
    arr_str = [str(val) for val in sorted(arr, reverse=True)]
    i = len(arr_str)
    solution = 0
    while i > 0:
        for val in permutations(arr_str, i):
            num = int(''.join([v for v in val]))

            if num % 3 == 0:
                solution = num
                break

        if solution is not 0: break
        i -= 1
    return solution