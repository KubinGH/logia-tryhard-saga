def kulki(string):
    string = "".join(char for char in string if char in ("c", "z"))
    target = ""
    reds, greens = string.count("c"), string.count("z")
    pairs = min(reds, greens)
    target = ("cz" * pairs) + ("c" * (reds - pairs)) + ("z" * (greens - pairs))
    result = 0
    return sum(string[i] == "c" and string[i] != target[i] for i in range(len(string)))

if __name__ == "__main__":
    print(kulki("czczczzz"))
    print(kulki("czczzczz"))
    print(kulki("zzzzzcc"))
    print(kulki("zzz"))
    print(kulki("zczczcczczzc"))
