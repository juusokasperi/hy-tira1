class PermutationTracker:
    def __init__(self):
        self.nums = set()
        self.max_value = 0
        self.duplicate = False

    def append(self, number):
        if number in self.nums:
            self.duplicate = True
        else:
            self.nums.add(number)
            if number > self.max_value:
                self.max_value = number
                
    def check(self):
        if self.duplicate:
            return False
        return self.max_value == len(self.nums)

if __name__ == "__main__":
    tracker = PermutationTracker()

    tracker.append(1)
    print(tracker.check()) # True

    tracker.append(4)
    print(tracker.check()) # False

    tracker.append(2)
    print(tracker.check()) # False

    tracker.append(3)
    print(tracker.check()) # True

    tracker.append(2)
    print(tracker.check()) # False

    tracker.append(5)
    print(tracker.check()) # False
