def zeroes_list(length):
    return [0 for _ in range(length)]

def make_hexagon(size):
    result = []
    csize = size * 2 - 1
    for i in range(size):
        result.append(zeroes_list(csize))
    csize -= 2
    while csize > 0:
        result.append(zeroes_list(csize))
        csize -= 2
    return result

def sign(number):
    return -1 if number < 0 else (1 if number > 0 else 0)

def list_sum(list1, list2):
    return [a + b for a, b in zip(list1, list2)]

def pole(size, moves):
    moves = [(a - 1, b - 1) for a, b in moves]
    hexagon = make_hexagon(size)
    pos = moves.pop(0)
    visited = {pos}
    for move in moves:
        idx = 0 if pos[0] != move[0] else 1
        mdir = [sign(move[i] - pos[i]) for i in range(2)]
        BLOCK = 0
        while pos != move:
            BLOCK += 1
            pos = tuple(list_sum(pos, mdir))
            if pos in visited:
                return [pos[0] + 1, pos[1] + 1]
            visited.add(pos)
    return 0




if __name__ == "__main__":
    tests = [(4, [[4, 7], [5, 6], [5, 4], [7, 2]]),
             (6, [[2, 3], [5, 6], [5, 4], [1, 4]])]
    for test in tests:
        r = pole(*test)
        print(r)