def find_number(numbers):
    if numbers[0] != numbers[1]:
        if numbers[0] == numbers[2]:
            return numbers[1]
        return numbers[0]
    common = numbers[0]

    n = len(numbers)
    for i in range (2, n):
        if numbers[i] != common:
            return numbers[i]

if __name__ == "__main__":
    print(find_number([1, 1, 1, 2])) # 2
    print(find_number([1, 1, 2, 1])) # 2
    print(find_number([1, 2, 1, 1])) # 2
    print(find_number([2, 1, 1, 1])) # 2
    print(find_number([5, 5, 5, 3, 5])) # 3
    print(find_number([1, 100, 1])) # 100

    numbers = [1] * 10**5 + [2]
    print(find_number(numbers)) # 2
