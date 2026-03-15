import time
import random

def find_mode_dict(numbers):
    count = {}
    mode = numbers[0]

    for x in numbers:
        if x not in count:
            count[x] = 0
        count[x] += 1

        if count[x] > count[mode]:
            mode = x

    return mode

def find_mode_sort(numbers):
    numbers = sorted(numbers)

    mode = numbers[0]
    max_count = -1

    curr_count = 0
    last_num = numbers[0]

    for num in numbers:
        if num == last_num:
            curr_count += 1
        else:
            curr_count = 1
        if curr_count > max_count:
            mode = num
            max_count = curr_count
        last_num = num
    return mode

if __name__ == "__main__":
    n = 10**7
    numbers = random.choices(range(1, 1001), k=10**7)

    times = []
    print("=== Mode Dict ===")
    for i in range(5):
        print("  Round ", i + 1)
        start_time = time.perf_counter()
        mode = find_mode_dict(numbers)
        times.append(time.perf_counter() - start_time)
    print(f"--> MIN: {min(times):.5f} s")
    print(f"--> AVG: {sum(times)/len(times):.5f} s")
    print(f">>> RESULT: {mode}\n")

    times = []
    print("=== Mode Sort ===")
    for i in range(5):
        print("  Round ", i + 1)
        start_time = time.perf_counter()
        mode = find_mode_sort(numbers)
        times.append(time.perf_counter() - start_time)
    print(f"--> MIN: {min(times):.5f} s")
    print(f"--> AVG: {sum(times)/len(times):.5f} s")
    print(f">>> RESULT: {mode}\n")
