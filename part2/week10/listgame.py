def first_wins(numbers):
    if not numbers:
        return False
    
    n = len(numbers)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = numbers[i]

    for length in range(2, n + 1):
        for left in range(n - length + 1):
            right = left + length - 1
            take_left = numbers[left] - dp[left + 1][right]
            take_right = numbers[right] - dp[left][right - 1]
            dp[left][right] = max(take_left, take_right)
    return dp[0][n - 1] > 0

if __name__ == "__main__":
    print(first_wins([2, 1, 3])) # True
    print(first_wins([1, 3, 1])) # False

    print(first_wins([1])) # True
    print(first_wins([1, 1])) # False
    print(first_wins([1, 5])) # True
    print(first_wins([1, 1, 1])) # True
    print(first_wins([1, 2, 3, 4])) # True
    print(first_wins([1, 3, 3, 7, 4, 2, 1])) # False

    print(first_wins([1] * 50)) # False
    print(first_wins([1, 2] * 25)) # True
