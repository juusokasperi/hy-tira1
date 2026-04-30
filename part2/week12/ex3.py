import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeSet:
    def __init__(self):
        self.root = None
        self.max_depth = -1

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            self.max_depth = 0
            return
        node = self.root
        curr_depth = 0
        while True:
            curr_depth += 1
            if node.value == value:
                return
            if node.value > value:
                if not node.left:
                    node.left = Node(value)
                    self.max_depth = max(self.max_depth, curr_depth) 
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = Node(value)
                    self.max_depth = max(self.max_depth, curr_depth) 
                    return
                node = node.right

    def height(self):
        return self.max_depth

if __name__ == "__main__":
    numbers = TreeSet()
    for i in range(1000):
        numbers.add(i + 1)
    height = numbers.height()
    print(f"--> Height when adding 1...1000 in order: {height}\n")

    numbers_random = TreeSet()
    nums = list(range(1000))
    random.shuffle(nums)
    for i in nums:
        numbers_random.add(i + 1)
    height = numbers_random.height()
    print(f"--> Height when adding 1...1000 in random order: {height}\n")
