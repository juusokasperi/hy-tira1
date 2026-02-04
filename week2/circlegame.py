def find_order(n):
    if n == 1:
        return [1]
    circle = list(range(1, n + 1))
    order = []
    skip = True

    while len(order) < n:
        out_circle = []
        for player in circle:
            if skip:
                out_circle.append(player)
                skip = False
            else:
                order.append(player)
                skip = True
        circle = out_circle
    return order

if __name__ == "__main__":
    print(find_order(1)) # [1]
    print(find_order(2)) # [2, 1]
    print(find_order(3)) # [2, 1, 3]
    print(find_order(7)) # [2, 4, 6, 1, 5, 3, 7]

    order = find_order(10**5)
    print(order[-5:]) # [52545, 85313, 36161, 3393, 68929]
