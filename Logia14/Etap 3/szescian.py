def obok(n, k):
    def to_coor(i):
        return i % n, (i // n) % n, (i // n**2) % n
    def to_number(x, y, z):
        return x + y*n + z*(n**2)
    k -= 1
    x, y, z = to_coor(k)
    result = []
    if x > 0:
        result.append((x-1, y, z))
    if y > 0:
        result.append((x, y-1, z))
    if z > 0:
        result.append((x, y, z-1))
    if x < n - 1:
        result.append((x+1, y, z))
    if y < n - 1:
        result.append((x, y+1, z))
    if z < n - 1:
        result.append((x, y, z+1))
    return sorted(to_number(cx, cy, cz)+1 for cx, cy, cz in result)

if __name__ == "__main__":
    print(obok(3, 11))
    print(obok(7, 1))
    print(obok(10, 1000))
