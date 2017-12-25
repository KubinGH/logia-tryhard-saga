from turtle import *
from math import sqrt

class NotDrawing:
    def __init__(self):
        pass
    def __enter__(self):
        self.is_down_before = isdown()
        pu()
        return self
    def __exit__(self, *args):
        if self.is_down_before: pd()

def sqrdiag(n):
    return sqrt(2) * n

def cipher(n, side):
    start = pos(); start_h = heading()
    def reset_t(start=start, start_h=start_h):
        with NotDrawing() as _:
            setpos(start); setheading(start_h)
    if 0 <= n <= 8:
        if n >= 0:
            right(45); forward(sqrdiag(side))
            with NotDrawing() as _:
                left(135); forward(side); left(135)
            forward(sqrdiag(side))
            
        if n >= 1:
            reset_t()
            with NotDrawing() as _: right(90)
            forward(side)
            
        if n >= 2:
            reset_t()
            with NotDrawing() as _: forward(side); right(90)
            forward(side)
            
        if n >= 3:
            reset_t()
            with NotDrawing() as _: forward(side / 2); right(90)
            forward(side)
            
        if n >= 4:
            reset_t()
            with NotDrawing() as _: right(90); forward(side); left(90)
            forward(side)
            
        if n >= 5:
            reset_t()
            forward(side)
            
        if n >= 6:
            reset_t()
            with NotDrawing() as _: right(90); forward(side / 2); left(90)
            forward(side)
            
        if n >= 7:
            reset_t()
            with NotDrawing() as _: forward(side / 4); right(90)
            forward(side)
            
        if n == 8:
            reset_t()
            with NotDrawing() as _: forward(3 * side / 4); right(90)
            forward(side)
            
    elif n == 9:
        for i in range(2):
            for s in (side / 2, side):
                forward(s); right(90)
    reset_t()

def ol(digits):
    TurtleScreen._RUNNING = True
    delay(0)
    digits = [int(i) for i in str(digits)]

    width = 720
    def this_width(n): return 1.5 if 0 <= n <= 8 else 1
    width_b =  sum(this_width(i) for i in digits) - 0.5
    side = width / width_b

    with NotDrawing() as _:
        back(width / 2); right(90)
        back(side / 2); left(90)
    
    for digit in digits:
        cipher(digit, side)
        with NotDrawing() as _:
            forward(this_width(digit) * side)

ol(989)
