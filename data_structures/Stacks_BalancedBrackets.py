def balanced(text):
    openers = {
        '{':'}',
        '(':')',
        '[':']',
    }
    stack = []

    for x in text:
        if x in openers:
            stack += x
        elif openers[stack[-1]] != x:
            return False
        else:
            stack.pop()

    return len(stack) == 0







# test = '{[()]}'
# test = '{[(])}'
test = '{{[[(())]]}}'

print('YES' if balanced(test) else 'NO')