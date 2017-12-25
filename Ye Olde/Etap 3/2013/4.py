def next_to(col, row):
    return [
        (col - 1, row),
        (col, row - 1),
        (col, row + 1),
        (col + 1, row)]

def valid_next_to(col, row, width, height):
    template = next_to(col, row)

    result = [(col, row) for col, row in template
              if 0 <= col < width and 0 <= row < height]

    return result

def next_to_diag(col, row):
    return [
        (col - 1, row - 1),
        (col - 1, row + 1),
        (col + 1, row - 1),
        (col + 1, row + 1)]

def valid_next_to_diag(col, row, width, height):
    template = next_to_diag(col, row)

    result = [(col, row) for col, row in template
              if 0 <= col < width and 0 <= row < height]

    return result

def asize(array):
    return (len(array[0]), len(array))

def lantern_works(light):
    return light > 0

def max_2d(array):
    maximum = float("-inf")
    pos = None
    for row, erow in enumerate(array):
        for col, elem in enumerate(erow):
            if elem > maximum:
                maximum = elem
                pos = (col, row)
    return pos

def maxj(array):
    width, height = asize(array)

    lanterns = [(col, row) for row, irow in enumerate(array)
                           for col, light in enumerate(irow)
                           if lantern_works(light)]

    light_map = [[0 for _ in range(width)] for _ in range(height)]

    for col, row in lanterns:
        light = array[row][col]
        args = (col, row, width, height)
        neighbours = valid_next_to(*args)
        neighbours_diag = valid_next_to_diag(*args)

        light_map[row][col] += light
        for ncol, nrow in neighbours:
            light_map[nrow][ncol] += light / 2
        for ncol, nrow in neighbours_diag:
            light_map[nrow][ncol] += light / 3

    mcol, mrow = max_2d(light_map)

    return (mrow + 1, mcol + 1)

if __name__ == "__main__":
    tests = [[[1, 2, 3, 2], [0, 0, 1, 2]],
             [[8, 1, 1], [4, 6, 0], [6, 2, 1]],
             [[1], [6], [3], [5], [3]]]

    for test in tests:
        print(test)
        r = maxj(test)
        print(r)