import time

if __name__ == "__main__":
    n = 10**5
    print(f"-- Adding {n} amount of numbers to list --")
    times = []
    for _ in range(5):
        lst = []
        start_time = time.perf_counter()
        for i in range(n):
            lst.append(i + 1)
        times.append(time.perf_counter() - start_time)
    print(f"--> MIN: {min(times):.5f} s")
    print(f"--> AVG: {sum(times)/len(times):.5f} s\n")

    times = []
    print(f"-- Deleting {n} amount of numbers to list --")
    for _ in range(5):
        lst = list(range(1, n + 1))
        start_time = time.perf_counter()
        for i in range(n):
            lst.pop(0)
        times.append(time.perf_counter() - start_time)
    print(f"--> MIN: {min(times):.5f} s")
    print(f"--> AVG: {sum(times)/len(times):.5f} s\n")
