import itertools

def count_numbers(length, numbers):
    num_list = sorted(list(set(numbers)))

    if length == 1:
        return len(num_list)
    if "0" in num_list:
        num_list.remove("0")
    if not num_list:
        return 0

    def backtrack(start_idx, curr_len):
        if curr_len == length:
            return 1
        
        total_valids = 0
        for i in range(start_idx, len(num_list)):
            total_valids += backtrack(i, curr_len + 1)
        return total_valids

    return backtrack(0, 0)

if __name__ == "__main__":
    print(count_numbers(3, "123")) # 10
    print(count_numbers(5, "1")) # 1
    print(count_numbers(2, "137")) # 6
    print(count_numbers(8, "25689")) # 495
    print(count_numbers(1, "0")) # 1
    print(count_numbers(2, "0")) # 0
    print(count_numbers(10, "12")) # 11
    print(count_numbers(10, "123456789")) # 43758
