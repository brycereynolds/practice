import string

def answer(s):
    alph = list(string.ascii_lowercase)
    alphr = list(reversed(alph))
    cypher = dict(zip(alph, alphr))

    chars = list(s)

    for i, val in enumerate(chars):
        chars[i] = cypher[chars[i]] if chars[i] in cypher else chars[i]

    return ''.join(chars)