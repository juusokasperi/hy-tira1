def find_first(size, steps):
    if size % 2 != 0:
        cycle = (size + 1) // 2
        idx = steps % cycle
        return 2 * idx + 1
    else:
        cycle = size
        idx = steps % cycle
        
        half = size // 2
        if idx < half:
            return 2 * idx + 1
        else:
            return 2 * (idx - half) + 2

if __name__ == "__main__":
    print(find_first(4, 3)) # 4
    print(find_first(12, 5)) # 11
    print(find_first(2, 1000)) # 1
    print(find_first(99, 555)) # 11
    print(find_first(12345, 10**6)) # 12295
    print(find_first(123456789, 1337**42)) # 111766959
