def find_boxes(boxes, products):
    events = []
    for size in boxes:
        events.append((size, 2, None))
    for index, size in enumerate(products):
        events.append((size, 1, index))
    events.sort()

    result = [-1] * len(products)
    heap = []
    for size, type, index in events:
        if type == 1:
            heapq.heappush(heap, index)
        if type == 2 and heap:
            result[heap[0]] = size
            heapq.heappop(heap)

    return result

if __name__ == "__main__":
    print(find_boxes([4, 4, 6, 8], [5, 5, 4, 6, 1]))
    # [6, 8, 4, -1, 4]

    print(find_boxes([1, 2, 3, 4], [1, 1, 1, 1, 1]))
    # [1, 2, 3, 4, -1]

    print(find_boxes([2, 2, 2, 2], [1, 1, 1, 1, 1, 1]))
    # [2, 2, 2, 2, -1, -1]

    print(find_boxes([1, 1, 1, 1], [2, 2]))
    # [-1, -1]

    boxes = []
    products = []
    for i in range(10**5):
        boxes.append(i % 100 + 1)
        products.append(3 * i % 97 + 1)
    result = find_boxes(boxes, products)

    boxes = [1000 * x for x in range(10**5)]
    products = [1000 * x for x in range(10**5)]
    result = find_boxes(boxes, products)
    print(result[42]) # 30
    print(result[1337]) # 35
    print(result[-1]) # 100
