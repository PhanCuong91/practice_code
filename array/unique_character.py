"""
Given a string, determine if it is comprised of all unique characters. For example, the string 'abcde' has all unique
characters and should return True. The string 'aabbcde' contains duplicate characters and should return False
"""


def unique_character(s):
    # create an array with 52 elements
    arr = [0]*52
    ind = 0
    if len(s) == 0:
        return False
    for i in s:
        # get index of character in array
        # upper case characters
        if ord(i) <= 90:
            ind = ord(i) - 65
        # lower case characters
        else:
            ind = ord(i) - 97 + 26
        # increase one if first appearance of character
        if arr[ind] < 1:
            arr[ind] += 1
        # if the second appearance, then return false
        else:
            return False
    return True


def uni_char(s):
    if len(s) == 0:
        return False
    chars = set()
    for i in s:
        if i in chars:
            return False
        else:
            chars.add(i)
    return True


print(unique_character('a'))
print(unique_character(''))
print(unique_character('aa'))
print(unique_character('adncb'))
print(unique_character('adncba'))

print('test other function')

print(uni_char('a'))
print(uni_char(''))
print(uni_char('aa'))
print(uni_char('adncb'))
print(uni_char('adncba'))