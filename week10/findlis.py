def find_sequence(numbers):
    if not numbers:
        return []

    n = len(numbers)
    lengths = [1] * n
    parent = [-1] * n

    longest_end_idx = 0
    max_len = 1

    for i in range(1, n):
        for j in range(i):
            if numbers[j] < numbers[i]:
                if lengths[j] + 1 > lengths[i]:
                    lengths[i] = lengths[j] + 1
                    parent[i] = j

        if lengths[i] > max_len:
            max_len = lengths[i]
            longest_end_idx = i

    seq = [0] * max_len
    curr = longest_end_idx
    write_idx = max_len - 1

    while curr != -1:
        seq[write_idx] = numbers[curr]
        curr = parent[curr]
        write_idx -= 1

    return seq

if __name__ == "__main__":
    print(find_sequence([1, 2, 3])) # [1, 2, 3]
    print(find_sequence([3, 2, 1])) # [1]
    print(find_sequence([1, 1, 1, 1, 1])) # [1]

    print(find_sequence([1, 8, 2, 7, 3, 6])) # [1, 2, 3, 6]
    print(find_sequence([1, 1, 2, 2, 3, 3])) # [1, 2, 3]
    print(find_sequence([4, 1, 5, 6, 3, 4, 3, 8])) # [1, 3, 4, 8]
