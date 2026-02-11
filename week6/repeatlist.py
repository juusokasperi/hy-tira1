class RepeatList:
    def __init__(self):
        self.nums = set()
        self._repeat = False

    def append(self, number):
        if number in self.nums:
            self._repeat = True
        else:
            self.nums.add(number)

    def repeat(self):
        return self._repeat

if __name__ == "__main__":
    numbers = RepeatList()

    print(numbers.repeat()) # False

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    print(numbers.repeat()) # False

    numbers.append(2)
    print(numbers.repeat()) # True

    numbers.append(5)
    print(numbers.repeat()) # True
