def count_pairs(numbers):
    numbers = sorted(numbers)
    n = len(numbers)
    i = 0
    j = n // 2
    result = 0
    while i < n // 2 and j < n:
        if 2 * numbers[i] <= numbers[j]:
            result += 1
            i += 1
            j += 1
        else:
            j += 1
    return result

if __name__ == "__main__":
    print(count_pairs([1])) # 0
    print(count_pairs([1, 2, 3])) # 1
    print(count_pairs([1, 2, 3, 4])) # 2
    print(count_pairs([1, 1, 1, 1])) # 0
    print(count_pairs([10**9, 1, 1, 1])) # 1
    print(count_pairs([4, 5, 1, 4, 7, 8])) # 2
    print(count_pairs([1, 2, 3, 2, 4, 6])) # 3

    numbers = [(x * 999983) % 10**6 + 1 for x in range(10**5)]
    print(count_pairs(numbers)) # 41176
