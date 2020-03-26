"""
Sort elements by frequency | Set 1
Print the elements of an array in the decreasing frequency
if 2 numbers have same frequency then print the one which came first.
Examples:
Input:  arr[] = {2, 5, 2, 8, 5, 6, 8, 8}
Output: arr[] = {8, 8, 8, 2, 2, 5, 5, 6}

Input: arr[] = {2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8}
Output: arr[] = {8, 8, 8, 2, 2, 5, 5, 6, -1, 9999999}
"""


def sort_frequency(arr):
    n = len(arr)
    count = [1]
    first = [arr[0]]
    j = 0
    for i in range(1, n):
        if arr[i] not in first:
            first.append(arr[i])
            count.append(1)
        else:
            id = first.index(arr[i])
            count[id] += 1
    print(count)
    print(first)
    n = len(count)
    for i in range(n-1):
        cur = i
        for j in range(i+1, n):
            if count[cur] < count[j]:
                cur = j
        if cur != i:
            temp = count[cur]
            count.pop(cur)
            count.insert(i, temp)
            temp = first[cur]
            first.pop(cur)
            first.insert(i, temp)

    print(count)
    print(first)
    index = 0
    for i in range(n):
        while count[i] != 0:
            arr[index] = first[i]
            index += 1
            count[i] -= 1

    return arr


print(sort_frequency([2, 5, 2, 8, 5, 6, 8, 8]))
print(sort_frequency([17, 22, 28, 25, 29, 4, 17, 46, 45, 13, 26, 32, 46, 3, 19, 30, 34, 18, 20, 25, 44, 44, 47, 10, 45, 9, 33, 13, 38, 21, 46, 8, 45, 33, 44, 15, 44, 23, 46, 47, 18, 33, 29, 5, 16, 24, 34, 47, 49, 9]))

"""
Given an array A[] consisting 0s, 1s and 2s. 
The task is to write a function that sorts the given array. 
The functions should put all 0s first, then all 1s and all 2s in last.
Examples:
Input: {0, 1, 2, 0, 1, 2}
Output: {0, 0, 1, 1, 2, 2}

Input: {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}
"""