def count_splits(numbers):
    uniques = len(set(numbers))
    n = len(numbers)

    seen = set()
    min_idx = -1
    for i in range(n - 1):
        seen.add(numbers[i])
        if len(seen) == uniques:
            min_idx = i + 1
            break

    if min_idx == -1:
        return 0

    seen = set()
    max_idx = -1
    for i in range(n - 1, 0, -1):
        seen.add(numbers[i])
        if len(seen) == uniques:
            max_idx = i
            break

    if max_idx < min_idx:
        return 0
    return max_idx - min_idx + 1

if __name__ == "__main__":
    print(count_splits([1, 1, 1, 1])) # 3
    print(count_splits([1, 1, 2, 1])) # 0
    print(count_splits([1, 2, 1, 2])) # 1
    print(count_splits([1, 2, 3, 4])) # 0
    print(count_splits([1, 2, 1, 2, 1, 2])) # 3

    numbers = [1, 2] * 10**5
    print(count_splits(numbers)) # 199997
    numbers = list(range(1, 10**5 + 1)) * 2
    print(count_splits(numbers)) # 1
