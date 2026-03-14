import itertools

def find_route(distances):
    n = len(distances)
    min_length = -1
    best_route = []

    for perm in itertools.permutations(range(1, n)):
        curr_len = 0
        curr_city = 0

        for next_city in perm:
            curr_len += distances[curr_city][next_city]
            curr_city = next_city
        curr_len += distances[curr_city][0]

        if curr_len < min_length or min_length == -1:
            min_length = curr_len
            best_route = [0] + list(perm) + [0]

    final_route = [city + 1 for city in best_route]

    return min_length, final_route

if __name__ == "__main__":
    distances = [[0, 2, 2, 1, 8],
                 [2, 0, 9, 1, 2],
                 [2, 9, 0, 8, 3],
                 [1, 1, 8, 0, 3],
                 [8, 2, 3, 3, 0]]

    length, route = find_route(distances)
    print(length) # 9
    print(route) # [1, 3, 5, 2, 4, 1]

    distances = [[0, 7, 5, 9, 6, 3, 1, 3],
                 [7, 0, 3, 2, 3, 3, 7, 8],
                 [5, 3, 0, 4, 2, 7, 7, 1],
                 [9, 2, 4, 0, 2, 3, 2, 4],
                 [6, 3, 2, 2, 0, 9, 5, 9],
                 [3, 3, 7, 3, 9, 0, 4, 5],
                 [1, 7, 7, 2, 5, 4, 0, 7],
                 [3, 8, 1, 4, 9, 5, 7, 0]]

    length, route = find_route(distances)
    print(length) # 18
    print(route) # [1, 7, 4, 6, 2, 5, 3, 8, 1]
