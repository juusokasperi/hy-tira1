class MaxList:
    def __init__(self):
        self.list = []
        self.max_idx = -1

    def append(self, number):
        self.list.append(number)
        if self.max_idx < 0 or number > self.list[self.max_idx]:
            self.max_idx = len(self.list) - 1

    def max(self):
        return self.list[self.max_idx]

if __name__ == "__main__":
    numbers = MaxList()

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    print(numbers.max()) # 3

    numbers.append(8)
    numbers.append(5)
    print(numbers.max()) # 8
