import itertools

def min_count(weights, max_weight):
    if not weights:
        return 0
    for w in weights:
        if w > max_weight:
            return -1

    abs_min = (sum(weights) + max_weight - 1) // max_weight
    result = float('inf')

    for permutation in itertools.permutations(weights):
        curr_bins = 1
        curr_w = 0

        for w in permutation:
            if curr_w + w <= max_weight:
                curr_w += w
            else:
                curr_bins += 1
                curr_w = w

        if curr_bins < result:
            result = curr_bins
            if result == abs_min:
                break
    return result

if __name__ == "__main__":
    print(min_count([2, 3, 3, 5], 7)) # 2
    print(min_count([2, 3, 3, 5], 6)) # 3
    print(min_count([2, 3, 3, 5], 5)) # 3
    print(min_count([2, 3, 3, 5], 4)) # -1

    print(min_count([], 1)) # 0
    print(min_count([1], 1)) # 1
    print(min_count([1, 1, 1, 1], 1)) # 4
    print(min_count([1, 1, 1, 1], 4)) # 1

    print(min_count([3, 4, 1, 2, 3, 3, 5, 9], 10)) # 3
