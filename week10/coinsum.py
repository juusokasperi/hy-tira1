def can_create(coins, target):
    result = [False] * (target + 1)
    result[0] = True
    
    for s in range(1, target + 1):
        for c in coins:
            if s - c >= 0 and result[s - c] == True:
                result[s] = True
                break

    return result[target]

if __name__ == "__main__":
    print(can_create([1, 2, 5], 13)) # True
    print(can_create([2, 4, 6], 13)) # False
    print(can_create([1], 42)) # True
    print(can_create([2, 4, 6], 42)) # True
    print(can_create([3], 1337)) # False
    print(can_create([3, 4], 1337)) # True
