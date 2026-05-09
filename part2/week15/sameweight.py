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
        if a == b: return

        if self.size[a] > self.size[b]:
            a, b = b, a
        self.link[a] = b
        self.size[b] += self.size[a]

class Kruskal:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = []

    def add_edge(self, node_a, node_b, weight):
        self.edges.append((node_a, node_b, weight))

    def construct(self, reverse=False):
        self.edges.sort(key=lambda x: x[2], reverse=reverse)

        uf = UnionFind(self.nodes)
        edges_count = 0
        tree_weight = 0

        for edge in self.edges:
            node_a, node_b, weight = edge
            if uf.find(node_a) != uf.find(node_b):
                uf.union(node_a, node_b)
                edges_count += 1
                tree_weight += weight

        if edges_count != len(self.nodes) - 1:
            return None
        return tree_weight


class SameWeight:
    def __init__(self, n):
        self.kruskal = Kruskal(range(1, n + 1))

    def add_edge(self, a, b, x):
        self.kruskal.add_edge(a,b,x)

    def check(self):
        min_weight = self.kruskal.construct()
        if min_weight is None:
            return True
        max_weight = self.kruskal.construct(reverse=True)
        return min_weight == max_weight

if __name__ == "__main__":
    same_weight = SameWeight(4)

    same_weight.add_edge(1, 2, 2)
    same_weight.add_edge(1, 3, 3)
    print(same_weight.check()) # True

    same_weight.add_edge(1, 4, 3)
    print(same_weight.check()) # True

    same_weight.add_edge(3, 4, 3)
    print(same_weight.check()) # True

    same_weight.add_edge(2, 4, 1)
    print(same_weight.check()) # False
