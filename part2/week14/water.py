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

def min_amount(left_volume, right_volume, target):
    if target > left_volume:
        return -1

    states = []
    for l in range(left_volume + 1):
        for r in range(right_volume + 1):
            states.append((l, r))
    solve = Dijkstra(states)

    for l, r in states:
        solve.add_edge((l, r), (left_volume, r), left_volume - l)
        solve.add_edge((l, r), (l, right_volume), right_volume - r)
        solve.add_edge((l, r), (0, r), l)
        solve.add_edge((l, r), (l, 0), r)

        pour_to_right = min(l, right_volume - r)
        solve.add_edge((l, r), (l - pour_to_right, r + pour_to_right), pour_to_right)
        
        pour_to_left = min(r, left_volume - l)
        solve.add_edge((l, r), (l + pour_to_left, r - pour_to_left), pour_to_left)

    all_dist = solve.find_distances((0, 0))

    min_cost = float("inf")
    for r in range(right_volume + 1):
        cost = all_dist.get((target, r), float("inf"))
        if cost < min_cost:
            min_cost = cost
    if min_cost == float("inf"):
        return -1
    return min_cost

if __name__ == "__main__":
    print(min_amount(5, 4, 2)) # 22
    print(min_amount(4, 3, 2)) # 16
    print(min_amount(3, 3, 1)) # -1
    print(min_amount(1, 1, 10**9)) # -1
    print(min_amount(10, 9, 8)) # 46
    print(min_amount(123, 456, 42)) # 10530
    print(min_amount(305, 117, 345))
