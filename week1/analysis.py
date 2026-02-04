import random
import time

def count_even_1(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

def count_even_2(numbers):
    return sum(x % 2 == 0 for x in numbers)

def benchmark(name, func, data, runs=5):
    times = []
    print(f"-- Testing {name} --")
    for i in range(5):
        start_time = time.time()
        func(data)
        end_time = time.time()
        duration = end_time - start_time
        times.append(duration)
    print(f"--> MIN: {min(times):.5f} s")
    print(f"--> AVG: {sum(times)/len(times):.5f} s\n")

if __name__ == "__main__":
    n = 10**7
    random.seed(42)
    numbers = [random.randint(-2147483648, 2147483647) for _ in range(n)]
    benchmark("Implementation 1", count_even_1, numbers)
    benchmark("Implementation 2", count_even_2, numbers)
