class DistanceTracker:
    def __init__(self):
        self.counts = {}
        self.index_sums = {}
        self.total_dist_sums = {}
        self.curr_size = 0

    def append(self, number):
        idx = self.curr_size
        k = self.counts.get(number, 0)
        prev_idx_sum = self.index_sums.get(number, 0)
        curr_total = self.total_dist_sums.get(number, 0)

        new_total = curr_total + (k * idx - prev_idx_sum)

        self.total_dist_sums[number] = new_total
        self.index_sums[number] = prev_idx_sum + idx
        self.counts[number] = k + 1
        self.curr_size += 1

    def sum(self, number):
        return self.total_dist_sums.get(number, 0)

if __name__ == "__main__":
    tracker = DistanceTracker()

    tracker.append(1)
    tracker.append(2)
    tracker.append(1)
    tracker.append(3)
    tracker.append(3)
    tracker.append(1)
    tracker.append(2)
    tracker.append(1)

    print(tracker.sum(1)) # 24
    print(tracker.sum(2)) # 5
    print(tracker.sum(3)) # 1

    tracker.append(1)
    tracker.append(2)
    tracker.append(3)

    print(tracker.sum(1)) # 42
    print(tracker.sum(2)) # 16
    print(tracker.sum(3)) # 14
