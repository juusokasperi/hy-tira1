def count_numbers(a, b):
    if a > b:
        return 0
    count = 0

    def generate(current_num):
        nonlocal count
        if a <= current_num <= b:
            count += 1

        for digit in [2, 5]:
            next_num = current_num * 10 + digit
            if next_num <= b:
                generate(next_num)

    generate(2)
    generate(5)
    return count

if __name__ == "__main__":
    print(count_numbers(1, 100)) # 6
    print(count_numbers(60, 70)) # 0
    print(count_numbers(25, 25)) # 1
    print(count_numbers(1, 10**9)) # 1022
    print(count_numbers(123456789, 987654321)) # 512
