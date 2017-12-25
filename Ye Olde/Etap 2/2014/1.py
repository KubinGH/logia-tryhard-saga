from turtle import *

#itertools.cycle
def cycle(iterable):
    elements = []
    for element in iterable:
        yield element
        elements.append(element)
    while True:
        for element in elements:
            yield element

def copy2d(lst):
    return [row.copy() for row in lst]

def sign(number):
    return abs(number) / number

def square(side):
    for _ in range(4):
        forward(side)
        right(90)

def spiral(lst, side):
    start = pos(); start_h = heading()
    fillcolor("green")
    for row in lst:
        for col in row:
            if col: begin_fill()
            square(side / 5); pu(); forward(side / 5); pd()
            if col: end_fill()
        pu(); back(side)
        right(90); forward(side / 5); left(90); pd()
    pu(); goto(start); setheading(start_h); pd()

def szyfruj(word, height_b):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    dirs = cycle([(0, -1), (1, 0), (0, 1), (-1, 0)])
    spirals = {}
    current = [[0 for _ in range(5)] for _ in range(5)] #5x5 filled with 0
    pointer = [0, 4]
    direction = next(dirs)

    spirals[alphabet[0]] = copy2d(current)
    for letter in alphabet[1:]:
        x, y = pointer
        current[y][x] = 1
        spirals[letter] = copy2d(current)
        if letter == alphabet[-1]: break
        correct = False
        while not correct:
            next_pointer = [p + d for p, d in zip(pointer, direction)]
            n_x, n_y = next_pointer
            if not (0 <= n_x <= 4) or not (0 <= n_y <= 4) or current[n_y][n_x]:
                direction = next(dirs)
            else:
                correct = True
        pointer = next_pointer


    TurtleScreen._RUNNING = True    
    width = 760; width_b = len(word)
    side = width / width_b
    height = side * height_b
    start = (-width // 2, height // 2)

    pu(); goto(start); pd()
    for row in range(height_b):
        for col in range(width_b):
            square(side); pu(); forward(side); pd()
        pu(); back(side * width_b)
        right(90); forward(side); left(90); pd()

    pu(); goto(start); pd()
    tpoint = 0
    tdirs = cycle([1, -1]) 
    tdir = next(tdirs)
    for letter in word:
        print(letter)
        spiral_lst = spirals[letter]
        spiral(spiral_lst, side)
        
        correct = False
        while not correct:
            next_tpoint = tpoint + tdir
            if not (0 <= next_tpoint < height_b):
                tdir = next(tdirs)
            else:
                correct = True
        tpoint = next_tpoint

        pu(); forward(side)
        right(90 * tdir); forward(side)
        left(90 * tdir); pd()
