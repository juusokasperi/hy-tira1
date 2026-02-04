def calculate(input, rules):
    instruction = list("L" + input + "R")
    state = 1
    pos = 0

    rule_map = {}
    for r_char, r_state, new_char, new_state, action in rules:
        rule_map[(r_char, r_state)] = (new_char, new_state, action)
    for _ in range(1000):
        if pos < 0 or pos >= len(instruction):
            return False
        current_char = instruction[pos]
        key = (current_char, state)
        if key not in rule_map:
            return False
        new_char, new_state, action = rule_map[key]
        instruction[pos] = new_char
        state = new_state
        if action == "ACCEPT":
            return True
        elif action == "REJECT":
            return False
        elif action == "LEFT":
            pos -= 1
        elif action == "RIGHT":
            pos += 1
    return False

def create_rules():
    START, FIND_L, RUN_R, MARK_R, RUN_L = 1, 2, 3, 4, 5
    RESET = 10
    PICK_UP, GOT_0, GOT_1, RETURN, SUCCESS = 20, 21, 22, 23, 24
    rules = []

    def move(state, chars, direction):
        for c in chars:
            rules.append((c, state, c, state, direction))
    
    rules.append(("L", START, "L", FIND_L, "RIGHT"))
    rules.append(("0", FIND_L, "A", RUN_R, "RIGHT"))
    rules.append(("1", FIND_L, "B", RUN_R, "RIGHT"))

    for c in ["X", "Y", "R"]:
        rules.append((c, FIND_L, c, RESET, "LEFT"))
    
    move(RUN_R, ["0", "1", "X", "Y"], "RIGHT")
    rules.append(("R", RUN_R, "R", MARK_R, "LEFT"))
    
    move(MARK_R, ["X", "Y"], "LEFT")
    rules.append(("0", MARK_R, "X", RUN_L, "LEFT"))
    rules.append(("1", MARK_R, "Y", RUN_L, "LEFT"))

    move(RUN_L, ["0", "1", "X", "Y"], "LEFT")
    rules.append(("A", RUN_L, "A", FIND_L, "RIGHT"))
    rules.append(("B", RUN_L, "B", FIND_L, "RIGHT"))
    
    move(RESET, ["A", "B", "X", "Y", "Z"], "LEFT")
    rules.append(("L", RESET, "L", PICK_UP, "RIGHT"))

    rules.append(("Z", PICK_UP, "Z", PICK_UP, "RIGHT"))
    rules.append(("A", PICK_UP, "Z", GOT_0, "RIGHT"))
    rules.append(("B", PICK_UP, "Z", GOT_1, "RIGHT"))

    rules.append(("X", PICK_UP, "X", SUCCESS, "ACCEPT"))
    rules.append(("Y", PICK_UP, "Y", SUCCESS, "ACCEPT"))
    rules.append(("R", PICK_UP, "R", SUCCESS, "ACCEPT"))

    move(GOT_0, ["A", "B", "Z"], "RIGHT")
    rules.append(("X", GOT_0, "Z", RETURN, "LEFT"))

    move(GOT_1, ["A", "B", "Z"], "RIGHT")
    rules.append(("Y", GOT_1, "Z", RETURN, "LEFT"))

    move(RETURN, ["A", "B", "X", "Y", "Z"], "LEFT")
    rules.append(("L", RETURN, "L", PICK_UP, "RIGHT"))

    return rules

    

if __name__ == "__main__":
    rules = create_rules()
    print(calculate("00", rules)) # True
    print(calculate("001001", rules)) # True
    print(calculate("10111011", rules)) # True
    print(calculate("01", rules)) # False
    print(calculate("00100", rules)) # False
    print(calculate("10111101", rules)) # False
