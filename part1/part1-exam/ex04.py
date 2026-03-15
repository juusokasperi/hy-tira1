def count_pairs(numbers):
    result = 0
    counts = {}

    for i in range (n):
        num = numbers[i]
        if num not in counts:
            counts[num] = 0
        result += i - counts[num]
        counts[num] += 1
    return result
