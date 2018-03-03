def cycle(iterable):
    while True:
        yield from iterable

def zipsum(a, b):
    return [x + y for x, y in zip(a, b)]

def spotkanie(first_cycle, second_cycle):
    dirs = {"g": (0, 1), "d": (0, -1), "p": (1, 0), "l": (-1, 0)}
    A, B = [0, 0], [0, 0]
    for a, b, i in zip(cycle(first_cycle), cycle(second_cycle), range(100)):
        A = zipsum(A, dirs[a])
        B = zipsum(B, dirs[b])
        if A == B:
            return i + 1
    return 0

if __name__ == "__main__":
    print(spotkanie("pd", "g"))
    print(spotkanie("gp", "pg"))
    print(spotkanie("dg", "ggppddll"))
