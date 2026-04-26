import time
import random
import heapq

if __name__ == "__main__":
    n = 10**7
    x = 10**9
    numbers = random.choices(range(1, x + 1), k=n)

    print("=== Sort list and count 10 first ===")
    start_time = time.perf_counter()
    num_sorted = sorted(numbers)
    result = 0
    for i in range(10):
        result += num_sorted[i]
    total_time = time.perf_counter() - start_time
    print(f"--> Time to sort a list and count 10 smallest: {total_time}s")

    print("=== Heap push one at a time and pop 10 ===")
    start_time = time.perf_counter()
    num_heap = []
    for num in numbers:
        heapq.heappush(num_heap, num)
    result = 0
    for i in range(10):
        result += heapq.heappop(num_heap)
    total_time = time.perf_counter() - start_time
    print(f"--> Time to heapify and pop 10 smallest: {total_time}s")

    print("=== Heapify and pop 10 ===")
    start_time = time.perf_counter()
    heapq.heapify(numbers)
    result = 0
    for i in range(10):
        result += heapq.heappop(numbers)
    total_time = time.perf_counter() - start_time
    print(f"--> Time to heapify and pop 10 smallest: {total_time}s")

