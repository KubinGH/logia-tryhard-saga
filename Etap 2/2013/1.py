from turtle import *

class FillingWrap:
    def __init__(self, this_color=None):
        self.this_color = this_color
    def __enter__(self):
        if self.this_color is not None:
            self.last_color = fillcolor()
            fillcolor(self.this_color)
            begin_fill()
        return self
    def __exit__(self, ttype, value, traceback):
        if self.this_color is not None:
            end_fill()
            fillcolor(self.last_color)

def square(side, fcolor=None):
    with FillingWrap(fcolor) as f:
        for _ in range(4):
            forward(side)
            right(90)

def rotate(alpha, lst, n):
    return [alpha[(alpha.find(c) + n) % len(alpha)] for c in lst]

def mozaika(colors, key, base):
    TurtleScreen._RUNNING = True
    colors_dict = {
        "c": "red",
        "z": "limegreen",
        "x": "black",
        "b": "white",
        "f": "purple"
    }

    base = list(base)
    lines = []
    lines.append(base)
    current = base.copy()
    for _ in range(len(colors)):
        current = rotate(colors, current, key)
        lines.append(current)
    
    height_b = len(colors) + 1
    width_b = len(base)
    width = 600
    side = width / width_b
    height = side * height_b

    pu(); goto(-width/2, height/2); pd()
    for line in lines:
        for c in line:
            square(side, colors_dict[c])
            pu(); forward(side); pd()
        pu(); back(width); right(90)
        forward(side); left(90); pd()
