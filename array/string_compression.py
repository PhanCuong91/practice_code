"""
Problem: given string in the form 'AAABBCCCDDDD' compress it to become 'A3B2C3D4'. The function  should be case
sensitive, so that string 'AAAaaa' return 'A3a3'
"""


def string_compression(string):
    count = 1
    char = string[0]
    res = ""
    index = 0
    if len(string) == 0:
        return ""
    if len(string) == 1:
        return string + '1'

    for i in string[1:]:
        if i != char:
            res += char + str(count)
            char = i
            count = 1
        else:
            count += 1
        index += 1
        if index == len(string) - 1:
            res += char + str(count)
    return res


def string_compression_2(s):
    res = ""
    l = len(s)
    cnt = 1
    i = 1
    if l == 0:
        return ""
    if l == 1:
        return s + '1'
    while i < l:
        if s[i] != s[i - 1]:
            res += s[i - 1] + str(cnt)
            cnt = 1
        else:
            cnt += 1
        i += 1
    res += s[i - 1] + str(cnt)
    return res


print(string_compression_2('A'))
print(string_compression_2('AAABBCCCDDDDEEE'))
