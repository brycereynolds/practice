# https://www.hackerrank.com/challenges/plus-minus

def calculate_signs(vals):
    pos = 0
    zero = 0
    neg = 0
    for i in vals:
        if i < 0:
            neg += 1
        elif i > 0:
            pos += 1
        else:
            zero += 1
    return {'neg':neg, 'zero':zero, 'pos':pos}

def precision_avg(val, n, precision):
    return '{0:.{1}f}'.format(val / n, precision)


vals = [-4,3,-9,0,4,1]
signs = calculate_signs(vals)

print(precision_avg(signs['pos'], len(vals), 6))
print(precision_avg(signs['neg'], len(vals), 6))
print(precision_avg(signs['zero'], len(vals), 6))