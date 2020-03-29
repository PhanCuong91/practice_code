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


# print(sort_frequency([2, 5, 2, 8, 5, 6, 8, 8]))
# print(sort_frequency([17, 22, 28, 25, 29, 4, 17, 46, 45, 13, 26, 32, 46, 3, 19, 30, 34, 18, 20, 25, 44, 44, 47, 10, 45, 9, 33, 13, 38, 21, 46, 8, 45, 33, 44, 15, 44, 23, 46, 47, 18, 33, 29, 5, 16, 24, 34, 47, 49, 9]))

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


# Python program for Bitonic Sort. Note that this program
# works only when size of input is a power of 2.

# The parameter dir indicates the sorting direction, ASCENDING
# or DESCENDING; if (a[i] > a[j]) agrees with the direction,
# then a[i] and a[j] are interchanged.*/
def compAndSwap(a, i, j, dire):
    if (dire == 1 and a[i] > a[j]) or (dire == 0 and a[i] < a[j]):
        a[i], a[j] = a[j], a[i]

    # It recursively sorts a bitonic sequence in ascending order,


# if dir = 1, and in descending order otherwise (means dir=0).
# The sequence to be sorted starts at index position low,
# the parameter cnt is the number of elements to be sorted.
def bitonicMerge(a, low, cnt, dire):
    if cnt > 1:
        k = int(cnt / 2)
        for i in range(low, low + k):
            compAndSwap(a, i, i + k, dire)
        bitonicMerge(a, low, k, dire)
        bitonicMerge(a, low + k, k, dire)

    # This funcion first produces a bitonic sequence by recursively


# sorting its two halves in opposite sorting orders, and then
# calls bitonicMerge to make them in the same order
def bitonicSort(a, low, cnt, dire):
    if cnt > 1:
        k = int(cnt / 2)
        bitonicSort(a, low, k, 1)
        bitonicSort(a, low + k, k, 0)
        bitonicMerge(a, low, cnt, dire)

    # Caller of bitonicSort for sorting the entire array of length N


# in ASCENDING order
def sort(a, N, up):
    bitonicSort(a, 0, N, up)


# Driver code to test above
a = [3, 7, 4, 8, 6, 2, 1, 9, 5, 10]
n = len(a)
up = 1

sort(a, n, up)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % a[i])