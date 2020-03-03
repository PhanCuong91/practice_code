"""
Problem: Give a string of words, reserve all the words. For example:
Given:
    "This is the best"
return:
    "tseb eht si sihT"

As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:
    '  space here ' and 'space here      '
    both becomes:
    'ereh ecaps'
"""


def remove_space(str):
    count = 0
    res = []
    # search space in string
    # and remove space if at least two continous space
    for i in str:
        if i == ' ':
            if count == 0:
                res.append(i)
                count += 1
        else:
            res.append(i)
            count = 0
    # remove space if first character is space
    if res[0] == ' ':
        res.pop(0)
    n = len(res)
    # remove if the last character is space
    if res[n-1] == ' ':
        res.pop(n-1)
    return res


def remove_space_2(str):
    space = [' ']
    start = 0
    res = []
    i = 0
    while i < (len(str)):
        if str[i] not in space:
            start = i
            while i < len(str) and str[i] not in space:
                i += 1
            res.append(str[start:i])
        i += 1
    return res


def sentence_reserve(str_1, str_2):
    # remove space in 2 strings
    str_1 = remove_space(str_1)
    str_2 = remove_space(str_2)
    # if length is not equal, then return false
    if len(str_1) != len(str_2):
        return False
    n = len(str_1) - 1
    # compare character
    for i in range(n):
        if str_1[i] != str_2[n-i]:
            return False
    return True


print(remove_space_2('  ad ad '))
print(sentence_reserve("  go for  ", "rof og     "))
print(sentence_reserve("  go for  ", "arof og     "))