def count_parts(songs):
    n = len(songs)
    last_seen = {}
    res = 0
    start_idx = 0

    for i in range(n):
        song = songs[i]
        if song in last_seen and last_seen[song] >= start_idx:
            start_idx = last_seen[song] + 1
        last_seen[song] = i
        curr_window_len = i - start_idx + 1
        res += curr_window_len
    return res


if __name__ == "__main__":
    print(count_parts([1, 1, 1, 1])) # 4
    print(count_parts([1, 2, 3, 4])) # 10
    print(count_parts([1, 2, 1, 2])) # 7
    print(count_parts([1, 2, 1, 3])) # 8
    print(count_parts([1, 1, 2, 1])) # 6

    songs = [1, 2] * 10**5
    print(count_parts(songs)) # 399999
    songs = list(range(1, 10**5 + 1)) * 2
    print(count_parts(songs)) # 15000050000
