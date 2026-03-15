def min_steps(x):
    if x == 1:
        return 0

    steps = [-1] * (x + 1)
    steps[1] = 0

    for i in range(1, x):
        if steps[i] != -1:
            if i + 3 <= x:
                if steps[i + 3] == -1:
                    steps[i + 3] = steps[i] + 1
                else:
                    steps[i + 3] = min(steps[i + 3], steps[i] + 1)
            if i * 2 <= x:
                if steps[i * 2] == -1:
                    steps[i * 2] = steps[i] + 1
                else:
                    steps[i * 2] = min(steps[i * 2], steps[i] + 1)
    return steps[x]

if __name__ == "__main__":
    print(min_steps(1)) # 0
    print(min_steps(2)) # 1
    print(min_steps(3)) # -1
    print(min_steps(4)) # 1
    print(min_steps(5)) # 2
    print(min_steps(17)) # 4
    print(min_steps(42)) # -1
    print(min_steps(100)) # 7
    print(min_steps(1000)) # 13
