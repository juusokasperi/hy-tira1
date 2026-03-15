class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

    def __repr__(self):
        return str(self.value)

def count_leaves(node):
    if not node.children:
        return 1
    count = 0
    for child in node.children:
        count += count_leaves(child)
    return count

if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(count_leaves(tree1)) # 4

