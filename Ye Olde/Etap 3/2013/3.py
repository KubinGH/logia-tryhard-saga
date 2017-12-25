def cycle(iterable):
    while True:
        yield from iterable

def does_cycle(iterable, items):
    for a, b in zip(iterable, cycle(items)):
        if a != b:
            return False
    return True

def is_cycling_bin_num(number):
    return does_cycle(number, ("1", "0"))

def cycle_n(iterable, length):
    return [item for _, item in zip(range(length), cycle(iterable))]

def cycle_bin(length):
    return "".join(cycle_n(("1", "0"), length))

def fbin(number):
    return bin(number)[2:]

def int_b2(number):
    return int(number, 2) if number else 0

def ileod(start_binary):
    if is_cycling_bin_num(start_binary):
        return "0"

    print("\ntest", start_binary)

    start_n = int_b2(start_binary)
    cycling = cycle_bin(len(start_binary))
    cycling_n = int_b2(cycling)

    if start_n < cycling_n:
        print("smaller")
        cycling_s = cycle_bin(len(start_binary) - 1)
        cycling_s_n = int_b2(cycling_s)
        return fbin(start_n - cycling_s_n)

    else:
        print("ok")
        return fbin(start_n - cycling_n)


if __name__ == "__main__":
    tests = ["101", "111", "1101", "1" * 30,
             "101010101010101010101010101001"]
    for test in tests:
        r = ileod(test)
        print(test, r)
        c = fbin(int_b2(test) - int_b2(r))
        print(c, len(c), len(test))
