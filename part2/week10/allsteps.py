def count_steps(x):
    if x < 1:
        return 0

    steps = [0] * (x + 1)
    steps[1] = 1

    for i in range(1, x):
        if steps[i] > 0:
            if i + 3 <= x:
                steps[i + 3] += steps[i]
            if i * 2 <= x:
                steps[i * 2] += steps[i]
    return steps[x]


if __name__ == "__main__":
    print(count_steps(1)) # 1
    print(count_steps(2)) # 1
    print(count_steps(3)) # 0
    print(count_steps(4)) # 2
    print(count_steps(5)) # 1
    print(count_steps(17)) # 5
    print(count_steps(42)) # 0
    print(count_steps(100)) # 242
    print(count_steps(1000)) # 2948311
