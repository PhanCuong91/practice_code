

def hash_index(value, n):
    if value >= 97:
        value -= 32
    index = int(value % n)
    return index


def anagram_sort(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    return sorted(s1) == sorted(s2)


def anagram_check_2(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    count = {}
    if len(s1) != len(s2):
        return False
    else:
        for i in s1:
            print(i)
            # if the key is in dictionary
            # then increase value of the key
            # cannot increase value of key
            # which is not defined the value
            if i in count:
                count[i] += 1
            # if the key is not in dictionary
            # then add the key and value
            else:
                count[i] = 1
        for i in s2:
            if i in count:
                count[i] -= 1
            else:
                count[i] = 1
        for x in count:
            if count[x] != 0:
                return False
        return True


def anagram_check(s1, s2):
    n = 65
    arr = [0] * n
    for i in s1:
        if ord(i) != 32:
            ind = hash_index(ord(i), n)
            arr[ind] += 1
    for i in s2:
        if ord(i) != 32:
            ind = hash_index(ord(i), n)
            arr[ind] -= 1
    for i in range(65):
        if arr[i] != 0:
            return False
    return True

s1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# for i in s1:
#     print(i)
#     print(hash_index(ord(i), 65))
s1 = 'public relations'
s2 = 'crap built on lies'
assert anagram_check_2(s1, s2) == True,"Test is failed"
assert anagram_sort(s1, s2) == True,"Test is failed"
s1 = "clint eastwooD"
s2 = "old west action"
assert anagram_check_2(s1, s2) == True,"Test is failed"
assert anagram_sort(s1, s2) == True,"Test is failed"