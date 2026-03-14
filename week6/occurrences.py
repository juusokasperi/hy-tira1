class OccurrenceTracker:
    def __init__(self):
        self.counts = {}
        self.frequencies = {}
        self.distinct_freq_c = 0

    def append(self, number):
        old_freq = self.counts.get(number, 0)
        new_freq = old_freq + 1
        self.counts[number] = new_freq

        if old_freq > 0:
            self.frequencies[old_freq] -= 1
            if self.frequencies[old_freq] == 0:
                self.distinct_freq_c -= 1

        self.frequencies[new_freq] = self.frequencies.get(new_freq, 0) + 1
        if self.frequencies[new_freq] == 1:
            self.distinct_freq_c += 1

    def count(self):
        return self.distinct_freq_c

if __name__ == "__main__":
    tracker = OccurrenceTracker()

    tracker.append(1)
    tracker.append(2)
    tracker.append(1)
    tracker.append(3)
    print(tracker.count()) # 2

    tracker.append(2)
    tracker.append(3)
    print(tracker.count()) # 1

    tracker.append(2)
    tracker.append(3)
    tracker.append(3)
    print(tracker.count()) # 3
