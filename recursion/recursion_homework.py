"""
Problem 1:
write recursive function which sum from 0 to n
"""


def recursive_sum(n):
    # base case
    if n == 0:
        return 0
    return n + recursive_sum(n-1)


print(recursive_sum(4))
"""
Problem 2:
write recursive function which sum all of individual digits in n
ex: n = 1234 -> sum =  1+2+3+4
"""


def recursive_sum_digit(n):
    # base case
    if n == 0:
        return 0
    m = int(n % 10)
    n = int((n - m)/10)
    return m + recursive_sum_digit(n)


print(recursive_sum_digit(1234))
"""
Problem 3:
input a string phrase and a list of word
output: print words which in list word and string phrase 

"""


def word_split(phrase, word, output):
    if len(phrase) == 0:
        return []
    for i in range(len(phrase)):
        if phrase[0:i+1] in word:
            output.append(phrase[0:i + 1])
            phrase = phrase.replace(phrase[0:i+1], '')
            break
        if i == len(phrase)-1:
            return []

    word_split(phrase, word, output)
    return output


print(word_split('themanran', ['the', 'man', 'ran'], []))
print(word_split('ilovedogsJohn', ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John'], []))
print(word_split('themanran', ['clown', 'ran', 'man'], []))


"""
reserve a string
'hello world' ---> 'dlrow olleh'
"""
def recursion_reserved_text(s):
    # base case:
    if len(s) == 1:
        return s[0]
    return recursion_reserved_text(s[1:]) + s[0]


print(recursion_reserved_text('hello world   123456789'))


def permute(s):
    res = []
    # base case
    if len(s) == 1:
        return s
    arr = permute(s[1:])
    for i in range(len(s)):
        for j in range(len(arr)):
            tmp = arr[j][0:i] + s[0] + arr[j][i:]
            res.append(tmp)
    return res


def permute_1(s):
    res = []
    # base case:
    if len(s) == 1:
        return s
    for i in range(len(s)):
        for per in permute_1(s[:i] + s[i+1:]):
            res.append(s[i] + per)
    return res


print(permute_1('abcd'))
print(permute('abcd'))


def fibonnaci(n, mem):

    if mem[n-1] == 0:
        if n == 1 or n == 2:
            mem[n-1] = 1
        else:
            mem[n-1] = fibonnaci(n-1, mem) + fibonnaci(n-2, mem)
    return mem[n-1]


n = 10
mem = [0]*n
print(fibonnaci(n, mem))


def coin_change(n, coins):
    out = []

    for i in range(len(coins), 0, -1):
        cnt = 0
        while n - coins[i-1] >= 0:
            n -= coins[i-1]
            cnt += 1
        if cnt != 0:
            out.append([coins[i-1], cnt])
        if n == 0:
            break
    print(out)


def recursive_coin_change(n, coins, out):
    if n == 0:
        return out
    cnt = 0
    while n - coins[len(coins)-1] >= 0:
        n -= coins[len(coins)-1]
        cnt += 1
    if cnt != 0:
        out.append([coins[len(coins)-1], cnt])

    recursive_coin_change(n, coins[:len(coins)-1], out)
    return out


def recursive_coin_change_1(n, coins):
    min_coins = n
    if n in coins:
        return 1
    cnt = 0
    for i in [c for c in coins if c<=n]:
        cnt = 1 + recursive_coin_change_1(n-i, coins)
        if min_coins > cnt:
            min_coins = cnt

    return min_coins


def recursive_coin_change_2(n, coins, known_res):
    min_coins = n
    if n in coins:
        return 1
    cnt = 0
    if known_res[n-1] != 0:
        return known_res[n-1]
    for i in [c for c in coins if c <= n]:
        cnt = 1 + recursive_coin_change_2(n - i, coins, known_res)
        if min_coins > cnt:
            min_coins = cnt
    known_res[n-1] = cnt
    return known_res[n-1]


coin_change(45, [1, 5, 10, 25])
coin_change(23, [1, 5, 10, 25])
coin_change(63, [1, 5, 10, 25])
print(recursive_coin_change(45, [1, 5, 10, 25], []))
print(recursive_coin_change(23, [1, 5, 10, 25], []))
print(recursive_coin_change(74, [1, 5, 10, 25], []))
n = 12
arr = [0]*n
print(recursive_coin_change_2(n, [1, 5, 10, 25], arr))
n = 23
arr = [0]*n
print(recursive_coin_change_2(23, [1, 5, 10, 25], arr))
n = 63
arr = [0]*n
print(recursive_coin_change_2(63, [1, 5, 10, 25], arr))
