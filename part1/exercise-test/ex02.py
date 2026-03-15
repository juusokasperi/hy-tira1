# Esimerkiksi jos lista on [1, 2, 1, 2, 1], haluttu tulos on 9, koska mahdolliset osalistat ovat [1] (3 kertaa), [2] (2 kertaa), [1, 2, 1] (2 kertaa), [2, 1, 2] ja [1, 2, 1, 2, 1].

def count_lists(numbers):
    count = 0
    counts = {}
    for num in numbers:
        if num not in counts:
            counts[num] = 0
        counts[num] += 1
        count += counts[num]
    return count

if __name__ == "__main__":
    print(count_lists([1, 2, 1, 2, 1]))
