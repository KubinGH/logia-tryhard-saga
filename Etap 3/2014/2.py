def make_number_cube(size):
    numbers = iter(range(1, size**3 + 1))
    return [[[next(numbers) for x in range(size)] for y in range(size)] for z in range(size)]

def find_3d(seq, to_find):
    for z, layer in enumerate(seq):
        for y, row in enumerate(layer):
            for x, elem in enumerate(row):
                if elem == to_find:
                    return (x, y, z)
    raise ValueError("Couldn't find")

def obok(size, number):
    cube = make_number_cube(size)
    #[layer.reverse() for layer in cube]    

    x, y, z = find_3d(cube, number)

    proper_idx = lambda x: 0 <= x < size
    result = []
    if proper_idx(x - 1):
        result.append(cube[z][y][x - 1])
    if proper_idx(x + 1):
        result.append(cube[z][y][x + 1])
    if proper_idx(y - 1):
        result.append(cube[z][y - 1][x])
    if proper_idx(y + 1):
        result.append(cube[z][y + 1][x])
    if proper_idx(z - 1):
        result.append(cube[z - 1][y][x])
    if proper_idx(z + 1):
        result.append(cube[z + 1][y][x])

    result.sort()
    
    return result
