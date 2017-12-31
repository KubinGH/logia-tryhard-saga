def abc(string, key, index):
    cstrings = set()
    for i in range(1, 2 ** len(string) + 1):
        cstring = ""
        k = 0
        for char in string:
            if i % 2:
                cstring += char
                if k < len(key) and char == key[k]:
                    k += 1
            i //= 2
        if k >= len(key):
            cstrings.add(cstring)
    cstrings = sorted(cstrings)
    return cstrings[index-1]
