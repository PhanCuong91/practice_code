"""
Problem:
Give an integer array, output all the unique pairs that sum up to a specific value k
So the input:
    pair_sum([1,2,3,3],4)
    would return 2 pairs:
    (1,3) and (2,2)
"""


def array_pair_sum(arr, sum):
    minus_arr = [0] * len(arr)
    result = []
    for i in range(len(arr)):
        minus_arr[i] = sum - arr[i]
    for i in range(len(arr)):

        print("i: ",i)
        print("minus :",(len(minus_arr)))
        if minus_arr[i] in arr:
            ind = arr.index(minus_arr[i])
            result.append((arr[i], arr[ind]))
            arr.pop(i)
            arr.pop(ind-1)

            minus_arr.pop(i)
            minus_arr.pop(ind-1)
        if i >= len(arr) - 1:
            return result
    return result


def arr_pair_sum_2(arr, sum):
    if len(arr) < 2:
        return
    seen = set()
    output = set()
    for num in arr:
        tar = sum - num
        if tar not in arr:
            seen.add(tar)
        else:
            output.add(((min(num, tar)), (max(num, tar))))
    print('\n'.join(map(str, list(output))))


arr = [1, 2, 3, 2, 4, 0]
sum_all = 4
print(arr_pair_sum_2(arr, sum_all))