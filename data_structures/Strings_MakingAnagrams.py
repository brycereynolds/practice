def str_to_count(text):
    tmp = {}
    for x in text:
        if x in tmp:
            tmp[x] += 1
        else:
            tmp[x] = 1
    return tmp

def string_diff(str1, str2):
    str2_cnt = str_to_count(str2)

    misses = []
    for x in str1:
        if x not in str2_cnt:
            misses.append(x)
        else:
            str2_cnt[x] -= 1
            if str2_cnt[x] is 0:
                del str2_cnt[x]

    tot_misses = len(misses)
    for x in str2_cnt:
        tot_misses += str2_cnt[x]

    return tot_misses



str1 = 'fcrxzwscanmligyxyvym'
str2 = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'

print(string_diff(str1, str2))