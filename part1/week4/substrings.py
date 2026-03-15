def count_substrings(string):
    substrings = set()
    n = len(string)

    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = string[i:j]
            substrings.add(substring)
    return len(substrings)

if __name__ == "__main__":
    print(count_substrings("aaaa")) # 4
    print(count_substrings("abab")) # 7
    print(count_substrings("abcd")) # 10
    print(count_substrings("abbbbbb")) # 13
    print(count_substrings("aybabtu")) # 26
    print(count_substrings("saippuakauppias")) # 110
