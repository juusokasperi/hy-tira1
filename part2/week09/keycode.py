import itertools

def valid_code(code, pattern):
    for i in range(4):
        if pattern[i] != '?' and code[i] != pattern[i]:
            return False
    return True

def find_codes(pattern):
    codes = []
    numbers = "123456789"
    
    for code_tuple in itertools.permutations(numbers, 4):
        code = "".join(code_tuple)
        if valid_code(code, pattern):
            codes.append(code)
    return sorted(codes)

if __name__ == "__main__":
    codes = find_codes("24?5")
    print(codes) # ['2415', '2435', '2465', '2475', '2485', '2495']

    codes = find_codes("1?2?")
    print(codes[:5]) # ['1324', '1325', '1326', '1327', '1328']
    print(len(codes)) # 42

    codes = find_codes("????")
    print(codes[:5]) # ['1234', '1235', '1236', '1237', '1238']
    print(len(codes)) # 3024
