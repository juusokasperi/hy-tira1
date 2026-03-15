class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def find_tree(grid):
    rows = len(grid)

    def get_char(row, col):
        if 0 <= row < rows and 0 <= col < len(grid[row]):
            return grid[row][col]
        return '.'
    def build_node(row, col):
        value = int(grid[row][col])
        children = []

        next_row = row + 1
        if get_char(next_row, col - 1) == '/':
            children.append(trace_branch(next_row, col - 1))
        if get_char(next_row, col) == '|':
            children.append(trace_branch(next_row, col))
        if get_char(next_row, col + 1) == '\\':
            children.append(trace_branch(next_row, col + 1))
        return Node(value, children)
    def trace_branch(row, col):
        curr_row, curr_col = row, col
        
        while True:
            char = get_char(curr_row, curr_col)
            if char.isdigit():
                return build_node(curr_row, curr_col)
            if char == '/':
                curr_row += 1
                curr_col -= 1
            elif char == '\\':
                curr_row += 1
                curr_col += 1
            elif char == '|':
                curr_row += 1
            else:
                return None

    for row in range(rows):
        for col in range(len(grid[row])):
            if grid[row][col].isdigit():
                return build_node(row, col)
    return None

if __name__ == "__main__":
    grid = [r"...........",
            r"...........",
            r"......5....",
            r"...../.\...",
            r"....3...\..",
            r"....|....1.",
            r"....2......"]
    tree = find_tree(grid)
    print(tree)
    # Node(5, [Node(3, [Node(2)]), Node(1)])

    grid = [r"....1.....",
            r".../.\....",
            r"..2...\...",
            r"..|....3..",
            r"..7.../|\.",
            r"./.\.4.5.6",
            r"8...9....."]
    tree = find_tree(grid)
    print(tree)
    # Node(1, [Node(2, [Node(7, [Node(8), Node(9)])]), Node(3, [Node(4), Node(5), Node(6)])])
