def len_valid_alternates(text, char_one, char_two):
    mates = {}
    mates[char_one] = char_two
    mates[char_two] = char_one

    is_valid = True
    expected = None
    for letter in text:
        if letter not in mates:
            continue

        if expected is None:
            count = 1
            expected = mates[letter]

        else:
            if letter != expected:
                is_valid = False
                break
            else:
                count += 1
                expected = mates[letter]

    return count if is_valid else False

def two_characters(text, unique):
    i = 0
    count = 0
    while i < len(unique):
        for j in range(i + 1, len(unique)):
            temp = len_valid_alternates(text, unique[i], unique[j])
            if temp and temp > count:
                count = temp
        i += 1

    return count



# a b e f

# (a,b) == 5
# (a,e) == Invalid
# (a,f) == 3
# (b,e) == Invalid
# (b,f) == Invalid
# (e,f) == Invalid

# Any character that is a repeat is auto-invalid

text = 'beabeefeab'
print(two_characters(text, list(set(text))))