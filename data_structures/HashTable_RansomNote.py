def count_words(text):
    text_cnt = {}
    for x in text:
        if x not in text_cnt:
            text_cnt[x] = 1
        else:
            text_cnt[x] += 1

    return text_cnt
def can_ransom(note, src):
    note = note.split(' ')
    src = src.split(' ')

    src_cnt = count_words(src)

    allow_note = True
    for x in note:
        if x in src_cnt:
            src_cnt[x] -= 1
            if src_cnt[x] is 0:
                del src_cnt[x]
        else:
            allow_note = False
            break

    return allow_note


src = 'give me one grand today night'
note = 'give one grand today'

print('Yes' if can_ransom(note, src) else 'No')