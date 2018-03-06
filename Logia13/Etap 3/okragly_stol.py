def ostatni(n, k):
    if n == 1:
        return 1
    next_to = {i: [i - 1, i + 1] for i in range(2, n)}
    next_to[1] = [n, 2]
    next_to[n] = [n - 1, 1]
    def skip(this, times):
        for i in range(times):
            this = next_to[this][1]
        return this
    current = skip(1, k - 1)
    while len(next_to) > 1:
        left, right = next_to[current][0], next_to[current][1]
        next_to[left][1] = right
        next_to[right][0] = left
        del next_to[current]
        current = skip(right, k - 1)
    return current

if __name__ == "__main__":
    print(ostatni(7, 3))
    print(ostatni(6, 2))
    print(ostatni(5, 10))
    print(ostatni(1, 10))
    print(ostatni(2, 2))
