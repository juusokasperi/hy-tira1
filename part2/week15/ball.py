class MaximumFlow:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {}
        for i in self.nodes:
            for j in self.nodes:
                self.graph[(i, j)] = 0

    def add_edge(self, node_a, node_b, capacity):
        self.graph[(node_a, node_b)] += capacity

    def add_flow(self, node, sink, flow):
        if node in self.seen:
            return 0
        self.seen.add(node)
        if node == sink:
            return flow
        for next_node in self.nodes:
            if self.flow[(node, next_node)] > 0:
                new_flow = min(flow, self.flow[(node, next_node)])
                inc = self.add_flow(next_node, sink, new_flow)
                if inc > 0:
                    self.flow[(node, next_node)] -= inc
                    self.flow[(next_node, node)] += inc
                    return inc
        return 0

    def construct(self, source, sink):
        self.flow = self.graph.copy()
        total = 0
        while True:
            self.seen = set()
            add = self.add_flow(source, sink, float("inf"))
            if add == 0:
                break
            total += add
        return total

class Ball:
    def __init__(self, n):
        self.n = n
        self.fulkerson = MaximumFlow(range(2 * n + 2))

        for i in range(1, n + 1):
            self.fulkerson.add_edge(0, i, 1)
            self.fulkerson.add_edge(i + n, 2 * n + 1, 1)

    def add_pair(self, a, b):
        self.fulkerson.add_edge(a, b + self.n, 1)

    def max_pairs(self):
        return self.fulkerson.construct(0, 2 * self.n + 1)

if __name__ == "__main__":
    ball = Ball(4)

    print(ball.max_pairs()) # 0

    ball.add_pair(1, 2)
    print(ball.max_pairs()) # 1

    ball.add_pair(1, 3)
    ball.add_pair(3, 2)
    print(ball.max_pairs()) # 2

    ball.add_pair(2, 1)
    print(ball.max_pairs()) # 3
