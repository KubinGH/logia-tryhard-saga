def abc(string):
    groups = []
    string = [char for char in string if char in {"n", "c", "z"}]
    if not string: return 0
    current_group = [string[0], 1]
    for char in string[1:]:
        if char not in {"n", "c", "z"}:
            continue
        elif char == current_group[0]:
            current_group[1] += 1
        else:
            groups.append(current_group)
            current_group = [char, 1]
    groups.append(current_group)
    result = sum(len(group) for group in groups)
    for mark_c in range(len(groups)):
        for mark_z in range(mark_c + 1, len(groups)):
            x = 0
            for i, group in enumerate(groups):
                if i < mark_c and group[0] != "n":
                    x += group[1]
                elif mark_c <= i < mark_z and group[0] != "c":
                    x += group[1]
                elif mark_z < i and group[0] != "z":
                    x += group[1]
            result = min(x, result)
    return result

if __name__ == "__main__":
    print(abc('nncnnbffbbbccczzzcz'))
    print(abc('zzzznnnnz'))
    print(abc("nnnnnnnnnnnnnncccccccccccccccccccczzzzzzzzzzzzzzzzzzz" * 100))
