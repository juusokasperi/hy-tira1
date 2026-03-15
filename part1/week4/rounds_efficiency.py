import time
import random

def count_rounds_list(numbers):
    n = len(numbers)
    pos = [0] * (n + 1)
    for i in range(n):
        pos[numbers[i]] = i
    rounds = 1

    for i in range(2, n + 1):
        if pos[i] < pos[i - 1]:
            rounds += 1

    return rounds

def count_rounds_dict(numbers):
    n = len(numbers)

    pos = {}
    for i, x in enumerate(numbers):
        pos[x] = i

    rounds = 1
    for i in range(1, n):
        if pos[i + 1] < pos[i]:
            rounds += 1

    return rounds

if __name__ == "__main__":
    n = 10**7
    numbers = list(range(1, n + 1))
    random.shuffle(numbers)

    times = []
    print("=== Count Rounds List ===")
    for i in range(5):
        print("  Round ", i + 1)
        start_time = time.perf_counter()
        rounds = count_rounds_list(numbers)
        times.append(time.perf_counter() - start_time)
    print(f"--> MIN: {min(times):.5f} s")
    print(f"--> AVG: {sum(times)/len(times):.5f} s\n")

    times = []
    print("=== Count Rounds Dict ===")
    for i in range(5):
        print("  Round ", i + 1)
        start_time = time.perf_counter()
        rounds = count_rounds_dict(numbers)
        times.append(time.perf_counter() - start_time)
    print(f"--> MIN: {min(times):.5f} s")
    print(f"--> AVG: {sum(times)/len(times):.5f} s")
