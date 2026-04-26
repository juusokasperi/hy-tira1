from collections import deque

def find_first(size, steps):
    items = deque(range(1, size + 1))
    for _ in range(steps):
        first_num = items.popleft()
        second_num = items.popleft()
        items.extend([second_num, first_num])
    return items.popleft()

if __name__ == "__main__":
    print(find_first(4, 3)) # 4
    print(find_first(12, 5)) # 11
    print(find_first(2, 1000)) # 1
    print(find_first(99, 555)) # 11
    print(find_first(12345, 10**6)) # 12295
