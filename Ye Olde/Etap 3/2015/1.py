def deszyfr(alpha, rects):
    return "".join((" "+alpha)[r[0] // 10] for r in sorted(rects, key=lambda x: x[1])).split(" ")
