def maxj(sources):
    width, height = min(len(row) for row in sources), len(sources)
    light = [[0 for _ in range(width)] for _ in range(height)]
    def valid_index(x, y):
        return 0 <= x < width and 0 <= y < height
    def next_to(x, y):
        return [c for c in ((x, y-1), (x, y+1), (x-1, y), (x+1, y)) if valid_index(*c)]
    def next_to_diag(x, y):
        return [c for c in ((x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)) if valid_index(*c)]
    for y in range(height):
        for x in range(width):
            light[y][x] += sources[y][x]
            for nx, ny in next_to(x, y):
                light[ny][nx] += sources[y][x] / 2
            for nx, ny in next_to_diag(x, y):
                light[ny][nx] += sources[y][x] / 3
    maxvalue, maxpos = -1, (-1, -1)
    for y in range(height):
        for x in range(width):
            if light[y][x] > maxvalue:
                maxpos = [x, y]
                maxvalue = light[y][x]
    return [maxpos[1] + 1, maxpos[0] + 1]

if __name__ == "__main__":
    print(maxj([[1, 2, 3, 2], [0, 0, 1, 2]]))
    print(maxj([[8, 1, 1], [4, 6, 0], [6, 2, 1]]))
    print(maxj([[1], [6], [3], [5], [3]]))

