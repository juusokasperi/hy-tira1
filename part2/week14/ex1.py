import random
from time import perf_counter

class BellmanFord:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = []

    def add_edge(self, node_a, node_b, weight):
        self.edges.append((node_a, node_b, weight))

    def find_distances(self, start_node):
        distances = {}
        for node in self.nodes:
            distances[node] = float("inf")
        distances[start_node] = 0

        num_rounds = len(self.nodes) - 1
        for _ in range(num_rounds):
            for edge in self.edges:
                node_a, node_b, weight = edge
                new_distance = distances[node_a] + weight
                if new_distance < distances[node_b]:
                    distances[node_b] = new_distance

        return distances

if __name__ == "__main__":
    n = 5000
    nodes = list(range(1, n + 1))
    bf = BellmanFord(nodes)

    temp_edges = []
    for a in range(1, n+1):
        for b in range(a + 1, min(a + 10, n + 1)):
            weight = random.randint(1, 1000)
            temp_edges.append((a, b, weight))

    random.shuffle(temp_edges)

    for a, b, w in temp_edges:
        bf.add_edge(a, b, w)

    start_time = perf_counter()
    distances = bf.find_distances(1)
    end_time = perf_counter() - start_time

    print(f"Algorithm took {end_time:.5}s")
