import re
import itertools

class Oracle:
    def __init__(self, code):
        self.code = code
        self.counter = 0

    def check_code(self, code):
        self.counter += 1
        if self.counter > 16:
            raise RuntimeError("too many check_code calls")

        if type(code) != str or not re.match("^[1-9]{4}$", code) or len(code) != len(set(code)):
            raise RuntimeError("invalid code for check_code")

        in_place = in_code = 0
        for pos in range(4):
            if code[pos] in self.code:
                if code[pos] == self.code[pos]:
                    in_place += 1
                else:
                    in_code += 1

        return in_place, in_code

def find_matches(codes, guess, in_place, in_code):
    new_codes = []

    for code in codes:
        curr_in_place = 0
        curr_in_code = 0
        for i in range(4):
            if guess[i] == code[i]:
                curr_in_place += 1
            elif guess[i] in code:
                curr_in_code += 1
        if curr_in_place == in_place and curr_in_code == in_code:
            new_codes.append(code)

    return new_codes

def find_code(oracle):
    numbers = "123456789"
    codes = ["".join(p) for p in itertools.permutations(numbers, 4)]

    while True:
        curr_guess = codes[0]
        in_place, in_code = oracle.check_code(curr_guess)

        if in_place == 4:
            return curr_guess
        codes = find_matches(codes, curr_guess, in_place, in_code)
    return -1

if __name__ == "__main__":
    # esimerkki oraakkelin toiminnasta
    oracle = Oracle("4217")
    print(oracle.check_code("1234")) # (1, 2)
    print(oracle.check_code("3965")) # (0, 0)
    print(oracle.check_code("4271")) # (2, 2)
    print(oracle.check_code("4217")) # (4, 0)

    # esimerkki funktion find_code toiminnasta
    oracle = Oracle("4217")
    code = find_code(oracle)
    print(code) # 4217
