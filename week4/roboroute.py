def analyze_route(grid):
    rows = len(grid)
    cols = len(grid[0])

    curr_row = curr_col = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'R':
                curr_row, curr_col = r, c
                break
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    curr_dir = 0

    visited_cells = set()
    visited_cells.add((curr_row, curr_col))

    visited_states = set()
    visited_states.add((curr_row, curr_col, curr_dir))

    while 42:
        dr, dc = dirs[curr_dir]
        next_row, next_col = curr_row + dr, curr_col + dc
        
        if not (0 <= next_row < rows and 0 <= next_col < cols):
            return len(visited_cells), True

        if grid[next_row][next_col] == '#':
            curr_dir = (curr_dir + 1) % 4
        else:
            curr_row, curr_col = next_row, next_col
            visited_cells.add((curr_row, curr_col))

        current_state = (curr_row, curr_col, curr_dir)
        if current_state in visited_states:
            return len(visited_cells), False
        visited_states.add(current_state)

if __name__ == "__main__":
    grid1 = [".#......",
             "..#.....",
             ".......#",
             "#.R.....",
             "......#."]
    print(analyze_route(grid1)) # (14, True)

    grid2 = ["........",
             ".##.....",
             ".......#",
             "#.R.....",
             "......#."]
    print(analyze_route(grid2)) # (12, False)
