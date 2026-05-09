WIP = 1
READY = 2

class CoursePlan:
    def __init__(self):
        self.nodes = []
        self.graph = {}

    def add_course(self, course):
        if course not in self.graph:
            self.nodes.append(course)
            self.graph[course] = []

    def add_requisite(self, course1, course2):
        self.graph[course1].append(course2)

    def find_order(self):
        self.result = []
        self.visited = {}
        for node in self.nodes:
            if not self.visit(node):
                return None
        return self.result[::-1]

    def visit(self, node):
        if self.visited.get(node) == WIP:
            return False
        if self.visited.get(node) == READY:
            return True
        self.visited[node] = WIP
        for next_node in self.graph[node]:
            if not self.visit(next_node):
                return False
        self.visited[node] = READY
        self.result.append(node)
        return True

if __name__ == "__main__":
    courses = CoursePlan()

    courses.add_course("Ohpe")
    courses.add_course("Ohja")
    courses.add_course("Tira")
    courses.add_course("Jym")

    courses.add_requisite("Ohpe", "Ohja")
    courses.add_requisite("Ohja", "Tira")
    courses.add_requisite("Jym", "Tira")

    print(courses.find_order()) # esim. [Ohpe, Jym, Ohja, Tira]

    courses.add_requisite("Tira", "Tira")

    print(courses.find_order()) # None
