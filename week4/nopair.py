def find_number(numbers):
    occurrences = {}

    for num in numbers:
        if num not in occurrences:
            occurrences[num] = 1
        else:
            occurrences[num] += 1
    for num, count in occurrences.items():
        if count % 2 != 0:
            return num
    return -1

if __name__ == "__main__":
    print(find_number([1, 2, 4, 1, 4])) # 2
    print(find_number([1])) # 1
    print(find_number([1, 1, 2, 2, 2])) # 2
    print(find_number([1, 2, 3, 1, 2])) # 3
    print(find_number([1, 2, 1, 2, 1, 2, 1])) # 2

    numbers = list(range(1, 10**5+1))
    print(find_number(numbers + [0] + numbers)) # 0
