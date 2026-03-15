def count_nodes(node):
    result = 0
    if len(node.children) >= 2:
        result = 1
    for child in node.children:
        result += count_nodes(child)
    return result
