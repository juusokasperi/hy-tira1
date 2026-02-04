class WordFinder:
    def set_grid(self, grid):
        self.grid = grid
        self.h = len(grid)
        self.w = len(grid[0]) if self.h > 0 else 0

    def count(self, word):
        if not self.grid or not word:
            return 0

        word_len = len(word)
        found_occurrences = set()

        directions = [
                (0, 1), (0, -1), (1, 0), (-1, 0),
                (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

        for y in range(self.h):
            for x in range(self.w):
                if self.grid[y][x] == word[0]:
                    for dy, dx in directions:
                        coords = []
                        match = True
                        for i in range(word_len):
                            ny, nx = y + i * dy, x + i * dx
                            if 0 <= ny < self.h and 0 <= nx < self.w and self.grid[ny][nx] == word[i]:
                                coords.append((ny, nx))
                            else:
                                match = False
                                break
                        if match:
                            found_occurrences.add(frozenset(coords))
        return len(found_occurrences)

if __name__ == "__main__":
    grid = ["TIRATIRA",
            "IRATIRAT",
            "RATIRATI",
            "ATIRATIR"]

    finder = WordFinder()
    finder.set_grid(grid)

    print(finder.count("TIRA")) # 7 
    print(finder.count("TA")) # 13
    print(finder.count("RITARI")) # 3
    print(finder.count("A")) # 8
    print(finder.count("AA")) # 6
    print(finder.count("RAITA")) # 0     
