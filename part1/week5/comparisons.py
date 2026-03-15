import math

class Comparer:
    def __init__(self, numbers):
        self.numbers = numbers
        self.counter = 0
        n = len(self.numbers)
        self.bound = n * math.floor(math.log2(n))

    def list_size(self):
        return len(self.numbers)

    def smaller(self, a, b):
        self.counter += 1
        if self.counter > self.bound:
            raise RuntimeError("too many comparisons")
        return self.numbers[a] < self.numbers[b]

def find_list(comparer):
    n = comparer.list_size();
    if n == 0:
        return []
    if n == 1:
        return [1]

    sorted = [0]
    for i in range(1, n):
        low = 0
        high = len(sorted)
        while low < high:
            mid = (low + high) // 2
            if comparer.smaller(i, sorted[mid]):
                high = mid
            else:
                low = mid + 1
        sorted.insert(low, i)
    result = [0] * n
    for i, orig_idx in enumerate(sorted):
        result[orig_idx] = i + 1
    return result

if __name__ == "__main__":
    comparer = Comparer([3, 1, 2, 4])
    numbers = find_list(comparer)
    print(numbers) # [3, 1, 2, 4]

    comparer = Comparer([1, 6, 2, 5, 3, 4])
    numbers = find_list(comparer)
    print(numbers) # [1, 6, 2, 5, 3, 4]

    comparer = Comparer([1, 3, 2])
    numbers = find_list(comparer)
    print(numbers) # [3, 1, 2, 4]
