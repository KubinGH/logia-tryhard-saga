def abc(string):
    string = [char for char in string if char in {"n", "c", "z"}]
    max_n = max_c = max_z = 0
    for char in string:
        if char == "n":
            max_n += 1
        elif char == "c":
            max_c = max(max_n, max_c) + 1
        else:
            max_z = max(max_n, max_c, max_z) + 1
    return len(string) - max(max_n, max_c, max_z)

if __name__ == "__main__":
    print(abc("nncnnbffbbbccczzzcz"))
    print(abc("zzzznnnnz"))
    print(abc("ncz" * 3000))
