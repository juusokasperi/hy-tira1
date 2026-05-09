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

def find_route(grid):
    rows = len(grid)
    cols = len(grid[0])

    valid_nodes = []
    start_node = None
    end_node = None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '#':
                continue
            node = (r, c)
            valid_nodes.append(node)
            if grid[r][c] == 'A':
                start_node = node
            elif grid[r][c] == 'B':
                end_node = node
    
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    solve = Dijkstra(valid_nodes)
    for r, c in valid_nodes:
        for delta_r, delta_c in directions:
            new_r, new_c = r + delta_r, c + delta_c
            if (new_r < 0 or new_r > rows or
                new_c < 0 or new_c > cols):
                continue
            if grid[new_r][new_c] == '#':
                continue
            if grid[new_r][new_c] == '*':
                weight = 1
            else:
                weight = 0
            solve.add_edge((r, c), (new_r, new_c), weight)
    results = solve.find_distances(start_node)
    result = results.get(end_node, float("inf"))
    if result == float("inf"):
        return -1
    return result

if __name__ == "__main__":
    grid = ["########",
            "#*A*...#",
            "#.*****#",
            "#.**.**#",
            "#.*****#",
            "#..*.B.#",
            "########"]
    print(find_route(grid)) # 2
