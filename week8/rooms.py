def count_rooms(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    count = 0

    def explore(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] == '#' or (r, c) in visited:
            return
        visited.add((r, c))
        explore(r + 1, c)
        explore(r - 1, c)
        explore(r, c + 1)
        explore(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.' and (r, c) not in visited:
                count += 1
                explore(r, c)
    return count

if __name__ == "__main__":
    grid = ["########",
            "#.#..#.#",
            "#####..#",
            "#...#..#",
            "########"]
    print(count_rooms(grid)) # 4

    grid = ["########",
            "#......#",
            "#.####.#",
            "#......#",
            "########"]
    print(count_rooms(grid)) # 1

    grid = ["########",
            "######.#",
            "##.#####",
            "########",
            "########"]
    print(count_rooms(grid)) # 2
