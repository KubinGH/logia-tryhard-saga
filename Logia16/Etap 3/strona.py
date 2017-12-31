def maxu(history):
    ends = []
    count = max_count = 0
    for start, length in history:
        while ends and min(ends) < start:
            ends.remove(min(ends))
            count -= 1
        ends.append(start + length)
        count += 1
        max_count = max(max_count, count)
    return max_count
