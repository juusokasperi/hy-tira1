from itertools import cycle
from re import match

def check_number(number):
    if not match("^0[0-9]{8}$", number):
        return False

    payload = number[:-1]
    check_digit = int(number[-1])
    
    weights = cycle([3, 7, 1])
    total_sum = sum(int(num) * weight for num, weight in zip(payload, weights))
    required_digit = (10 - (total_sum % 10)) % 10
    return required_digit == check_digit

if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False
    print(check_number("5350961940")) # False
    print(check_number("100000007")) # False
