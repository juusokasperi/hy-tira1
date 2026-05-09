class UnionFind:
    def __init__(self, n):
        self.link = list(range(n+1))
        self.size = [1] * (n+1)

    def find(self, x):
        if self.link[x] == x:
            return x
        self.link[x] = self.find(self.link[x])
        return self.link[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b: return False

        if self.size[a] > self.size[b]:
            a, b = b, a
        self.link[a] = b
        self.size[b] += self.size[a]
        return True

class NewRoads:
    def __init__(self, n):
        self.n = n
        self.roads = []

    def add_road(self, a, b, x):
        self.roads.append((a, b, x))

    def min_cost(self):
        self.roads.sort(key = lambda road: road[2])

        uf = UnionFind(self.n)
        cost = 0
        count = 0
        
        for a, b, x in self.roads:
            if uf.union(a,b):
                cost += x
                count += 1

        if count == self.n - 1:
            return cost
        return -1

if __name__ == "__main__":
    new_roads = NewRoads(4)

    new_roads.add_road(1, 2, 2)
    new_roads.add_road(1, 3, 5)
    print(new_roads.min_cost()) # -1

    new_roads.add_road(3, 4, 4)
    print(new_roads.min_cost()) # 11

    new_roads.add_road(2, 3, 1)
    print(new_roads.min_cost()) # 7
