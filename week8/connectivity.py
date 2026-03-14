def connected(nodes, edges):
    graph = {node: [] for node in nodes}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    count = 0
    components = {}

    def visit(node):
        if node in components:
            return
        components[node] = count
        for next_node in graph[node]:
            visit(next_node)

    for node in nodes:
        if node not in components:
            count += 1
            visit(node)
    return count == 1

if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (2, 4), (2, 5), (3, 4), (4, 5)]
    print(connected(nodes, edges)) # True

    nodes = [1, 2, 3, 4, 5, 6, 7, 8]
    edges = [(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7)]
    print(connected(nodes, edges)) # False

    nodes = [1, 2, 3, 4, 5]
    edges = []
    print(connected(nodes, edges)) # False

    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
    print(connected(nodes, edges)) # True
