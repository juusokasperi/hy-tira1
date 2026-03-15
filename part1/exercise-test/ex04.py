def min_removals(number):
    n = len(numbers)
    pos = {}
    result = 1
    for i in range(n):
        num = numbers[i]
        if num in pos:
            result = max(result, i - pos[num] + 1)
        pos[num] = i
    return n - result

if __name__ == "__main__":

