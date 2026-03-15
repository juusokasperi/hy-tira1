def count_sequences(numbers):
    if not numbers:
        return 0

    n = len(numbers)
    lengths = [1] * n
    counts = [1] * n

    max_len = 1

    for i in range(1, n):
        for j in range(i):
            if numbers[j] < numbers[i]:
                if lengths[j] + 1 > lengths[i]:
                    lengths[i] = lengths[j] + 1
                    counts[i] = counts[j]
                elif lengths[j] + 1 == lengths[i]:
                    counts[i] += counts[j]

        if lengths[i] > max_len:
            max_len = lengths[i]

    total = 0
    for i in range(n):
        if lengths[i] == max_len:
            total += counts[i]
    return total


if __name__ == "__main__":
    print(count_sequences([1, 2, 3])) # 1
    print(count_sequences([3, 2, 1])) # 3
    print(count_sequences([1, 1, 1, 1, 1])) # 5

    print(count_sequences([1, 8, 2, 7, 3, 6])) # 1
    print(count_sequences([1, 1, 2, 2, 3, 3])) # 8
    print(count_sequences([4, 1, 5, 6, 3, 4, 3, 8])) # 3

