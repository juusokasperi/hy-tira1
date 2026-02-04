def find_rounds(numbers):
    n = len(numbers)
    pos = [0] * (n + 1)
    for i in range(n):
        pos[numbers[i]] = i
    rounds = []
    current_round = [1]

    for i in range(2, n + 1):
        if pos[i] < pos[i - 1]:
            rounds.append(current_round)
            current_round = []
        current_round.append(i)

    rounds.append(current_round)
    return rounds

if __name__ == "__main__":
    print(find_rounds([1, 2, 3, 4]))
    # [[1, 2, 3, 4]]

    print(find_rounds([1, 3, 2, 4]))
    # [[1, 2], [3, 4]]    

    print(find_rounds([4, 3, 2, 1]))
    # [[1], [2], [3], [4]]
    
    print(find_rounds([1]))
    # [[1]]

    print(find_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
    # [[1], [2, 3], [4, 5, 6], [7, 8]]
