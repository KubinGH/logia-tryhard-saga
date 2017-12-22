def pascal(lines, pos):
    line_idx = lines - 1; pos -= 1 #fix indexes
    triangle = [[1]]
    def new_line(t):
        t.append([0 for _ in range(len(t[-1]) + 1)])

    while len(triangle) != lines:
        new_line(triangle)
        this_line = len(triangle[-1])

        for i in range(this_line):
            if 0 <= i <= 3 or this_line - 4 <= i <= this_line - 1: pass
            else: continue
            
            if i < this_line - 1:
                triangle[-1][i] += triangle[-2][i]
            if -1 < i - 1:
                triangle[-1][i] += triangle[-2][i - 1]

    return triangle[line_idx][pos]
