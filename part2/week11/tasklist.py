import heapq

class Tasks:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, priority):
        heapq.heappush(self.tasks, (-priority, name))

    def fetch_task(self):
        return heapq.heappop(self.tasks)[1]

if __name__ == "__main__":
    tasks = Tasks()

    tasks.add_task("siivous", 20)
    tasks.add_task("koodaus", 90)
    tasks.add_task("treffit", 80)

    print(tasks.fetch_task()) # koodaus

    tasks.add_task("nukkuminen", 20)

    print(tasks.fetch_task()) # treffit
    print(tasks.fetch_task()) # nukkuminen
