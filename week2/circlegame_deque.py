from collections import deque

def find_order(n):
    if n == 1:
        return [1]
    circle = deque(range(1, n + 1))
    order = []

    while circle:
        circle.rotate(-1)
        order.append(circle.popleft())
    return order

if __name__ == "__main__":
    print(find_order(1)) # [1]
    print(find_order(2)) # [2, 1]
    print(find_order(3)) # [2, 1, 3]
    print(find_order(7)) # [2, 4, 6, 1, 5, 3, 7]

    order = find_order(10**5)
    print(order[-5:]) # [52545, 85313, 36161, 3393, 68929]
