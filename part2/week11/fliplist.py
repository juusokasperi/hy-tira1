from collections import deque

class FlipList:
    def __init__(self):
        self.items = deque()
        self.is_reverse = False

    def __repr__(self):
        as_list = list(self.items)
        if self.is_reverse:
            as_list.reverse()
        return str(as_list)

    def add_first(self, x):
        if self.is_reverse:
            self.items.append(x)
        else:
            self.items.appendleft(x)

    def add_last(self, x):
        if self.is_reverse:
            self.items.appendleft(x)
        else:
            self.items.append(x)

    def flip(self):
        self.is_reverse = not self.is_reverse

        # TODO

if __name__ == "__main__":
    numbers = FlipList()

    numbers.add_last(1)
    numbers.add_last(2)
    numbers.add_last(3)
    print(numbers) # [1, 2, 3]

    numbers.add_first(4)
    print(numbers) # [4, 1, 2, 3]

    numbers.flip()
    print(numbers) # [3, 2, 1, 4]

    numbers.add_last(5)
    print(numbers) # [3, 2, 1, 4, 5]
