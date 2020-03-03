

def word_split(str, word):
    res = []
    if word == []:
        return ''
    else:
        if word[0] in str:
            tmp = word[0]
            str.replace(tmp, '')
            word.remove(tmp)
            if tmp != '':
                res.append(tmp)
                word_split(str, word)

        else:
            res = []
    return res


print(word_split('themanran', ['the', 'man', 'ran']))
