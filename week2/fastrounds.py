def count_rounds(numbers):
    n = len(numbers)
    pos = [0] * (n + 1)
    for i in range(n):
        pos[numbers[i]] = i
    rounds = 1

    for i in range(2, n + 1):
        if pos[i] < pos[i - 1]:
            rounds += 1

    return rounds

if __name__ == "__main__":
    print(count_rounds([1, 2, 3, 4])) # 1
    print(count_rounds([1, 3, 2, 4])) # 2
    print(count_rounds([4, 3, 2, 1])) # 4
    print(count_rounds([1])) # 1
    print(count_rounds([2, 1, 4, 7, 5, 3, 6, 8])) # 4

    n = 10**5
    numbers = list(reversed(range(1, n+1)))
    print(count_rounds(numbers)) # 100000
