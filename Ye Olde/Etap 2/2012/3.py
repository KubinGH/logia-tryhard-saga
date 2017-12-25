#docs -> itertools
def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)

def swaps(elems, key):
    key = {e: i for i, e in enumerate(key)}
    f = {e: i for i, e in enumerate(elems)}
    elems = list(elems)
    changed = True
    swaps = 0
    while changed:
        changed = False
        for i in range(len(elems) - 1):
            if key[elems[i]] > key[elems[i + 1]]:
                elems[i], elems[i + 1] = elems[i + 1], elems[i]
                changed = True
                swaps += 1
    return swaps
    
def miasta(a, t, z):
    a = tuple(a); t = tuple(t); z = tuple(z)
    ways = list(permutations(a))
    best = {"way": None, "negatives": float("INF")}

    for way in ways:
        negatives = sum(swaps(c, way) for c in (a, t, z))
        if negatives < best["negatives"]:
            best["negatives"] = negatives
            best["way"] = way


    return "".join(best["way"]), best["negatives"]

print(miasta("PŁKW", "WPŁK", "PWKŁ"))
print(miasta("TSG", "TGS", "GST"))
