class Contest:
    def __init__(self, names, task_count):
        self.names = names
        self.scores = {name: [0] * task_count for name in names}
        self.times = {name: 0 for name in names}
        self.clock = 0

    def add_submission(self, name, task, score):
        self.clock += 1
        task_index = task - 1
        old_score = self.scores[name][task_index]
        if score > old_score:
            self.scores[name][task_index] = score
            self.times[name] = self.clock

    def create_scoreboard(self):
        def get_total_score(name):
            return sum(self.scores[name])
        def order_criteria(name):
            total = get_total_score(name)
            time = self.times[name]
            return (-total, time, name)
        sorted_names = sorted(self.names, key=order_criteria)
        result = []
        for name in sorted_names:
            result.append((name, get_total_score(name)))
        return result


if __name__ == "__main__":
    names = ["anna", "pekka", "kalle", "tiina", "eeva"]
    contest = Contest(names, 3)

    contest.add_submission("tiina", 2, 30)
    contest.add_submission("pekka", 1, 40)
    contest.add_submission("tiina", 1, 20)
    contest.add_submission("pekka", 1, 50)
    contest.add_submission("pekka", 2, 0)
    contest.add_submission("eeva", 3, 100)
    contest.add_submission("anna", 1, 0)
    contest.add_submission("eeva", 3, 80)
    contest.add_submission("tiina", 2, 30)

    scoreboard = contest.create_scoreboard()
    print(scoreboard)
    # [('eeva', 100), ('tiina', 50), ('pekka', 50), ('anna', 0), ('kalle', 0)]
