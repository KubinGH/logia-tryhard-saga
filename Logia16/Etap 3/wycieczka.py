# Oh for fuck's sake

def opis(second_or_last, last):
    n = len(last)
    j = 0
    tree = {k: [None, None] for k in last}
    def firstempty(x): return x.index(None)
    parent_flag = False
    for i in range(n):
        a, b = last[i], second_or_last[j]
        if a == b: # Leaf
            parent_flag = True
            j += 1

    for k, v in tree.items():
        print(k, v)

print(opis([4,2,1,3,5,6],[1,2,3,4,6,5]))
