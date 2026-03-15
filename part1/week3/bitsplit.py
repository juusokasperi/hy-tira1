def count_splits(sequence):
    res = 0
    bal = 0

    n = len(sequence)
    for i in range(n):
        if sequence[i] == '0':
            bal -= 1
        else:
            bal += 1
        if bal == 0 and i < n -1:
            res += 1
    return res if bal == 0 else 0

if __name__ == "__main__":
    print(count_splits("00")) # 0
    print(count_splits("01")) # 0
    print(count_splits("0110")) # 1
    print(count_splits("010101")) # 2
    print(count_splits("000111")) # 0
    print(count_splits("01100110")) # 3

    sequence = "01"*10**5
    print(count_splits(sequence)) # 99999
