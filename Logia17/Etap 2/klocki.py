def kolit(string):
    size = 1
    rows = []
    while string:
        rows.append(string[:size])
        string = string[size:] if len(string) > size else ""
        size += 1
    result = 0
    for i in range(max(len(row) for row in rows)):
        all_equal = True
        last = None
        for row in rows:
            if len(row) <= i:
                continue
            elif last is None:
                last = row[i]
            elif last != row[i]:
                all_equal = False
                break
        result += all_equal
    return result

if __name__ == "__main__":
    print(kolit('ABCDEFGH'))
    print(kolit('ALAMAKRABY'))
