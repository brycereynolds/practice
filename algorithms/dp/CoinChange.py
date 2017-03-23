def change(C, n, m, memo = {}):
    if n == 0:
        return 1
    elif n <= 0:
        return 0
    elif m <= 0 and n >= 0:
        return 0
    elif n in memo:
        if m in memo[n]:
            return memo[n][m]

    if n not in memo:
        memo[n] = {}

    memo[n][m] = change(C, n, m - 1) + change(C, n - C[m - 1], m)
    return memo[n][m]

n = 4
C = [1,2,3]

# n = 10
# C = [2,5,3,6]

print(change(C, n, len(C)))


