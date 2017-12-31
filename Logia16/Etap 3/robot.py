#itertools.cycle
def cycle(iterable):
    items = list(iterable)
    while True:
        yield from items

def zipsum(a, b):
    return list(x + y for x, y in zip(a, b))

def lnp(n, y, x):
    x -= 1; y -= 1
    result = n**2 - 1
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[y][x] = True
    dirs = cycle(((1, 0), (0, 1), (-1, 0), (0, -1)))
    cdir = next(dirs)
    stopped_once = False
    while True:
        nx, ny = zipsum((x, y), cdir)
        if not (0 <= nx < n and 0 <= ny < n) or visited[ny][nx]:
            if stopped_once:
                break
            else:
                stopped_once = True
                cdir = next(dirs)
                continue
        else:
            stopped_once = False
            visited[ny][nx] = True
            result -= 1
            x, y = nx, ny
    return result
