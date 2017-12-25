def yielder(iterable):
    yield from iterable

def cube_from_str(string, side):
    gen = yielder(string)
    result = [[[next(gen) for _ in range(side)] for _ in range(side)] for _ in range(side)]
    for layer in result:
        layer.reverse()
    return result

def cube_find_all(cube, to_find):
    for z, layer in enumerate(cube):
        for y, row in enumerate(layer):
            for x, elem in enumerate(row):
                if elem == to_find:
                    yield (x, y, z)

def print_cube(cube):
    for i, layer in enumerate(cube):
        print("layer {}".format(i))
        for row in layer:
            print(row)   

def manhattan(first, second):
    return sum(abs(a - b) for a, b in zip(first, second))

def pionek(cubestr):
    SIDE = 3
    POINT_CHAR = "c"
    assert len(cubestr) == SIDE ** 3; assert cubestr.count(POINT_CHAR) == 2
    cube = cube_from_str(cubestr, SIDE)
    first, second = list(cube_find_all(cube, POINT_CHAR))
    distance = manhattan(first, second)



if __name__ == "__main__":
    tests = ["cbbbbbbbbbbbbbbbbbbbbbbbbbc",
             "bbbbbbbbbbbbbbbbbbbcbbbbbbc"]

    for test in tests:
        r = pionek(test)
        print(r)