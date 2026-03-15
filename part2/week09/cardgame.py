def count_combinations(cards, target):
    if target == 0:
        return 1
    if target < 0 or not cards:
        return 0

    current_card = cards[0]
    remaining_cards = cards[1:]

    include_card = count_combinations(remaining_cards, target - current_card)
    exclude_card = count_combinations(remaining_cards, target)

    return include_card + exclude_card
    
if __name__ == "__main__":
    print(count_combinations([2, 1, 4, 6], 6)) # 2
    print(count_combinations([1, 1, 1, 1], 2)) # 6
    print(count_combinations([2, 1, 4, 6], 15)) # 0
    print(count_combinations([1], 1)) # 1
    print(count_combinations([1, 2, 3, 4, 5], 5)) # 3
    print(count_combinations([1, 1, 4, 1, 1], 4)) # 2
    print(count_combinations([1] * 10, 5)) # 252
