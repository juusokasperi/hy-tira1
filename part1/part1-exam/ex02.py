def count_pairs(numbers):
    result = 0
    counts = {}

    for num in numbers:
        pair = 10 - num
        if pair in counts:
            result += counts[pair]
        if num not in counts:
            counts[num] = 0
        counts[num] += 1
    return result
