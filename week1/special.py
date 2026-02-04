def check_year(year):
    if year == 0:
        return True

    res = 0
    while year > 0:
        res += (year % 10) * (year % 10)
        year //= 10

    last_digit = res % 10

    while res > 0:
        curr_digit = res % 10
        if curr_digit != last_digit:
            return False
        res //= 10
    return True


if __name__ == "__main__":
    print(check_year(1995)) # False
    print(check_year(2000)) # True
    print(check_year(2026)) # True
    print(check_year(2029)) # False
    print(check_year(9215)) # True
