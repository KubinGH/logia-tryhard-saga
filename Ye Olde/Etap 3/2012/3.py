#itertools.permutations
def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

def no_neighbouring_same(sequence):
    for item1, item2 in zip(sequence, sequence[1:]):
        if item1 == item2:
            return False
    return True

def coral_permutations(quantity):
    basic = "".join(key * value for key, value in quantity.items())
    for p in permutations(basic):
        current = "".join(p)
        if no_neighbouring_same(current):
            yield current

def unique_list(iterable):
    return list(set(iterable))

def kulki(quantity_numbers):
    colors = "rgby"
    quantity = {key: value for key, value in zip(colors, quantity_numbers)}
    return sorted(unique_list(coral_permutations(quantity)))

if __name__ == "__main__":
    tests = [[2, 1, 1, 0]]
    for test in tests:
        r = kulki(test)
        print(r)