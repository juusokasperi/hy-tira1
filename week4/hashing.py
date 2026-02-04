def hash_value(string):
    n = len(string) - 1
    A = 23
    M = 2**32
    result = 0

    for char in string:
        char_val = ord(char) - ord('a')
        result += char_val * A**n
        n -= 1
    return result % M

if __name__ == "__main__":
    print(hash_value("abc")) # 25
    print(hash_value("kissa")) # 2905682
    print(hash_value("aybabtu")) # 154753059
    print(hash_value("tira")) # 235796
    print(hash_value("zzzzzzzzzz")) # 2739360440
