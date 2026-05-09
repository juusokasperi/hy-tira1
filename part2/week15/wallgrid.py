class UnionFind:
    def __init__(self, nodes):
        self.link = {node: None for node in nodes}
        self.size = {node: 1 for node in nodes}

    def find(self, x):
        while self.link[x]:
            x = self.link[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b: 
            return False

        if self.size[a] > self.size[b]:
            a, b = b, a
        self.link[a] = b
        self.size[b] += self.size[a]
        return True

class WallGrid:
    def __init__(self, n):
        self.n = n
        self.uf = UnionFind(range(1, n * n + 1))
        self.rooms = 0
        self.is_floor = [False] * (n * n + 1)

    def create_floor(self, x, y):
        i = (x - 1) * self.n + y
        if self.is_floor[i]: return

        self.is_floor[i] = True
        self.rooms += 1
        
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy

            if 1 <= nx <= self.n and 1 <= ny <= self.n:
                n_i = (nx - 1) * self.n + ny

                if self.is_floor[n_i]:
                    if self.uf.union(i, n_i):
                        self.rooms -= 1

    def count_rooms(self):
        return self.rooms

if __name__ == "__main__":
    wall_grid = WallGrid(5)

    print(wall_grid.count_rooms()) # 0

    wall_grid.create_floor(2, 2)
    wall_grid.create_floor(4, 2)
    print(wall_grid.count_rooms()) # 2

    wall_grid.create_floor(3, 2)
    print(wall_grid.count_rooms()) # 1

    wall_grid.create_floor(2, 4)
    wall_grid.create_floor(2, 4)
    wall_grid.create_floor(4, 4)
    print(wall_grid.count_rooms()) # 3

    wall_grid.create_floor(3, 3)
    print(wall_grid.count_rooms()) # 3

    wall_grid.create_floor(3, 4)
    print(wall_grid.count_rooms()) # 1

