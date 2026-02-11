class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def ancestor(node, a, b):
    def find_node(curr_node, target_val):
        if curr_node.value == target_val:
            return curr_node
        for child in curr_node.children:
            found = find_node(child, target_val)
            if found:
                return found
        return None
    def search_subtree(subtree_root, target_val):
        if subtree_root.value == target_val:
            return True
        for child in subtree_root.children:
            if search_subtree(child, target_val):
                return True
        return False
    node_a = find_node(node, a)
    if node_a is None:
        return False
    return search_subtree(node_a, b)

if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(ancestor(tree1, 1, 3)) # True
    print(ancestor(tree1, 2, 6)) # True
    print(ancestor(tree1, 3, 1)) # False
    print(ancestor(tree1, 5, 6)) # False
    print(ancestor(tree1, 3, 3)) # True

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(ancestor(tree2, 1, 4)) # True
    print(ancestor(tree2, 3, 2)) # False

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(ancestor(tree3, 1, 2)) # True
    print(ancestor(tree3, 1, 1)) # True
    print(ancestor(tree3, 2, 1)) # False
    print(ancestor(tree3, 5, 5)) # False
