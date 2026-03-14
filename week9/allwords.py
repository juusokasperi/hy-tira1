import itertools

def valid_word(w):
    for i in range(len(w) - 1):
        if w[i] == w[i + 1]:
            return False
    return True

def create_words(word):
    words = itertools.permutations(word, len(word))
    uniques = set()
    result = []

    for w in words:
        w = "".join(w)

        if w not in uniques and valid_word(w):
            result.append(w)
            uniques.add(w)

    return sorted(result)

if __name__ == "__main__":
    print(create_words("abc")) # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print(create_words("aab")) # ['aba']
    print(create_words("aaab")) # []

    print(create_words("kala"))
    # ['akal', 'akla', 'alak', 'alka', 'kala', 'laka']

    print(create_words("syksy"))
    # ['ksysy', 'kysys', 'skysy', 'syksy', 'sykys', 'sysky', 
    #  'sysyk', 'yksys', 'ysksy', 'yskys', 'ysyks', 'ysysk']

    print(len(create_words("aybabtu"))) # 660
    print(len(create_words("abcdefgh"))) # 40320
