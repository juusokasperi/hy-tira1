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

def find_other(string):
    new_val = hash_value(string) + 2**32

    while 42:
        temp_val = new_val
        chars = []

        while temp_val > 0:
            digit = temp_val % 23
            chars.append(chr(digit + ord('a')))
            temp_val //= 23
        new_string = "".join(reversed(chars))
        if new_string != string:
            return new_string
        new_val += 2**32
    

if __name__ == "__main__":
    string1 = "kissa"
    string2 = find_other("kissa")
    print(string1, hash_value(string1)) # kissa 2905682
    print(string2, hash_value(string2)) # zfgjynuk 2905682
