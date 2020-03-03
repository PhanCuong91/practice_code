"""
Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and
deleting a random element. Give these two arrays, find which element is missing in second array.
So the input:
    finder([1,2,3,4,5], [1,2,5,4])
    would return 3 which number is missing in first array
"""


def finder(arr1, arr2):
    out = set()
    for num in arr1:
        if num not in arr2:
            out.add(num)
    for num in arr2:
        if num not in arr1:
            out.add(num)
    print('\n'.join(map(str, list(out))))


def finder_2(arr1, arr2):
    d = {}
    out = set()
    for num in arr2:
        d[num] = 1
    for num in arr1:
        if num not in d:
            out.add(num)
    d = {}
    for num in arr1:
        d[num] = 1
    for num in arr2:
        if num not in d:
            out.add(num)
    print('\n'.join(map(str, list(out))))


s1 = [1,3,4,5,2]
s2 = [1,2,4,5,7]
finder_2(s1, s2)