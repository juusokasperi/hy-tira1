from collections import deque
from time import perf_counter

if __name__ == "__main__":
    items = deque()
    n = 10**5

    print("=== Add numbers 1 to 10**5 ===")
    start_time = perf_counter()
    for i in range(n):
        items.append(i)
    add_time = perf_counter() - start_time

    start_time = perf_counter()
    for i in range(len(items)):
        items.popleft()
    remove_time = perf_counter() - start_time

    print(f"--> Time to add {n} numbers to deque: {add_time}s\n")
    print(f"--> Time to remove {n} numbers to deque: {remove_time}s\n")
