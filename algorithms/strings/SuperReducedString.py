def reduce_string(text):
    last = len(text) - 1

    while last > 0:
        if text[last - 1] == text[last]:
            text = text[0:last - 1] + text[last + 1:]
            last = len(text) - 1
        else:
            last -= 1

    return text

string = 'aaabccddd'
print(reduce_string(string))