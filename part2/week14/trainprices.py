class FloydWarshall:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {}
        for a in self.nodes:
            for b in self.nodes:
                distance = 0 if a == b else float("inf")
                self.graph[(a, b)] = distance

    def add_edge(self, a, b, w):
        self.graph[(a, b)] = min(self.graph[(a, b)], w)

    def find_distances(self):
        distances = self.graph.copy()

        for k in self.nodes:
            for a in self.nodes:
                for b in self.nodes:
                    distance = min(distances[(a, b)],
                                   distances[(a, k)] +
                                   distances[(k, b)])
                    distances[(a, b)] = distance

        return distances

class TrainPrices:
    def __init__(self):
        self.cities = []
        self.edges = []

    def add_city(self, name):
        if name not in self.cities:
            self.cities.append(name)

    def add_train(self, city1, city2, price):
        self.edges.append((city1, city2, price))

    def find_prices(self):
        sorted_names = sorted(self.cities)
        fw = FloydWarshall(sorted_names)

        for c1, c2, p in self.edges:
            fw.add_edge(c1, c2, p)
            fw.add_edge(c2, c1, p)

        final_distances = fw.find_distances()

        table = [[None] + sorted_names]

        for city_a in sorted_names:
            row = [city_a]
            for city_b in sorted_names:
                dist = final_distances[(city_a, city_b)]
                row.append(int(dist) if dist != float("inf") else -1)
            table.append(row)

        return table

if __name__ == "__main__":
    prices = TrainPrices()

    prices.add_city("Helsinki")
    prices.add_city("Turku")
    prices.add_city("Tampere")
    prices.add_city("Oulu")

    prices.add_train("Helsinki", "Tampere", 20)
    prices.add_train("Helsinki", "Turku", 10)
    prices.add_train("Tampere", "Turku", 50)

    print(prices.find_prices())

    # metodin haluttu tulos:
    # [[None,       'Helsinki', 'Oulu', 'Tampere', 'Turku'],
    #  ['Helsinki', 0,          -1,     20,        10],
    #  ['Oulu',     -1,         0,      -1,        -1],
    #  ['Tampere',  20,         -1,     0,         30],
    #  ['Turku',    10,         -1,     30,        0]]
