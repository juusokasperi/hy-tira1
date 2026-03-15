def count_strings(n):
    if n < 1:
        return 0

    abc = [1] * 26

    for _ in range(n - 1):
        next_abc = [0] * 26

        next_abc[0] = abc[1]
        next_abc[25] = abc[24]

        for i in range(1, 25):
            next_abc[i] = abc[i - 1] + abc[i + 1]
        abc = next_abc
    return sum(abc)

if __name__ == "__main__":
    print(count_strings(1)) # 26
    print(count_strings(2)) # 50
    print(count_strings(3)) # 98
    print(count_strings(4)) # 192

    print(count_strings(42)) # 36766943673096
    print(count_strings(100)) # 7073450400109633000218032957656
