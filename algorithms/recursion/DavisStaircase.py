def climb_stairs(n, mono={}):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif n in mono:
        return mono[n]

    mono[n] = climb_stairs(n - 1, mono) + climb_stairs(n - 2, mono) + climb_stairs(n - 3, mono)
    return mono[n]

S = [1,3]
n = 7

print(climb_stairs(S, n))

def climb_stairs(S, n, mono={}):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif n in mono:
        return mono[n]

    val = 0
    for step_choice in S:
        val += climb_stairs(S, n - step_choice, mono)
    mono[n] = val
    return mono[n]

S = [1,3]
n = 7

print(climb_stairs(S, n))