class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeSet:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, value):
        self.size += 1
        if not self.root:
            self.root = Node(value)
            return
        node = self.root
        while True:
            if node.value == value:
                self.size -= 1
                return
            if node.value > value:
                if not node.left:
                    node.left = Node(value)
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = Node(value)
                    return
                node = node.right

    def __len__(self):
        return self.size

if __name__ == "__main__":
    numbers = TreeSet()
    print(len(numbers)) # 0
    numbers.add(1)
    print(len(numbers)) # 1
    numbers.add(2)
    print(len(numbers)) # 2
    numbers.add(3)
    print(len(numbers)) # 3
    numbers.add(2)
    print(len(numbers)) # 3
