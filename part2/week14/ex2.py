import random
from time import perf_counter
import heapq

class Dijkstra:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in nodes}

    def add_edge(self, node_a, node_b, weight):
        self.graph[node_a].append((node_b, weight))

    def find_distances(self, start_node):
        distances = {}
        for node in self.nodes:
            distances[node] = float("inf")
        distances[start_node] = 0

        queue = []
        heapq.heappush(queue, (0, start_node))

        visited = set()
        while queue:
            node_a = heapq.heappop(queue)[1]
            if node_a in visited:
                continue
            visited.add(node_a)

            for node_b, weight in self.graph[node_a]:
                new_distance = distances[node_a] + weight
                if new_distance < distances[node_b]:
                    distances[node_b] = new_distance
                    new_pair = (new_distance, node_b)
                    heapq.heappush(queue, new_pair)

        return distances

if __name__ == "__main__":
    n = 5000
    nodes = list(range(1, n + 1))
    bf = Dijkstra(nodes)

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

    print(f"Algorithm took {end_time:.3}s")
