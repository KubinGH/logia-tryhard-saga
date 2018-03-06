def ileod(binary):
    n = int(binary, 2)
    x = 0
    one_flag = 1
    while (x << 1) + one_flag <= n:
        x <<= 1
        x += one_flag
        one_flag ^= 1
    return bin(n - x)[2:]

if __name__ == "__main__":
    for i in range(32):
        print(i, bin(i), ileod(bin(i)), bin(i - int(ileod(bin(i)), 2)))
    print(ileod("101"))
    print(ileod("111"))
    print(ileod("1101"))
