class Connections:
    def __init__(self, n):
        self.n = n
        self.graph = {}
        for i in range(n):
            self.graph[i + 1] = []
        self.rev_graph = {}
        for i in range(n):
            self.rev_graph[i + 1] = []

    def add_link(self, a, b):
        self.graph[a].append(b)
        self.rev_graph[b].append(a)

    def check_network(self):
        def can_reach_all(graph, n):
            visited = set()
            stack = [1]
            visited.add(1)

            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
            return len(visited) == n

        if not can_reach_all(self.graph, self.n):
            return False
        if not can_reach_all(self.rev_graph, self.n):
            return False
        return True

if __name__ == "__main__":
    connections = Connections(5)

    connections.add_link(1, 2)
    connections.add_link(2, 3)
    connections.add_link(1, 3)
    connections.add_link(4, 5)

    print(connections.check_network()) # False

    connections.add_link(3, 5)
    connections.add_link(1, 4)

    print(connections.check_network()) # False

    connections.add_link(5, 1)

    print(connections.check_network()) # True
