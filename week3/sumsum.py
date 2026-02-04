def count_sum(numbers):
    n = len(numbers)
    result = 0
    for i in range(n):
        num_starts = i + 1
        num_ends = n - i
        frequency = num_starts * num_ends
        result += numbers[i] * frequency
    return result

if __name__ == "__main__":
    print(count_sum([1, 2, 3])) # 20
    print(count_sum([42])) # 42
    print(count_sum([1, 1, 1, 1])) # 20
    print(count_sum([2, 1, 7, 8, 5, 1, 3, 1])) # 484

    numbers = list(range(1, 10**5))
    print(count_sum(numbers)) # 8333333332500000000
