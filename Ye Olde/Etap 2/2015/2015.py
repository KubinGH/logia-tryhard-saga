from turtle import *


def szyfr(alphabet, subject):
    TurtleScreen._RUNNING = True
    vowels = "aeiouy"
    class rect_struct:
        def __init__(self, width, height, side):
            self.width = width; self.height = height; self.side = side
        def __iter__(self):
            return iter([self.width, self.height, self.side])
    def width_func(idx):   return (idx + 1) * 10            
    def height_func(letter): return (alphabet.find(letter) + 1) * 10
    def side_func(letter):  return 1 if letter not in vowels else -1

    def draw_rect(width, height, side):
        for _ in range(2):
            for length in (width, height):
                forward(length)
                left(90 * side)
    
    rectangles = [rect_struct(width_func(i), height_func(letter), side_func(letter))
                  for i, letter in enumerate(subject)]

    pu()
    max_height = max(rect.height * rect.side for rect in rectangles)
    min_height = min(rect.height * rect.side for rect in rectangles)
    left(90); back((max_height + min_height) / 2); right(90)
    back(sum(rect.width for rect in rectangles) / 2)
    pd()
    for width, height, side in rectangles:
        draw_rect(width, height, side)
        pu(); forward(width); pd()

def redukcja(number):
    number = list(str(number))[::-1]
    changing = True
    while changing:
        changing = False
        idx = 0
        while idx < len(number) - 1:
            if number[idx]  == number[idx + 1]:
                changing = True
                number.pop(idx + 1)
                number[idx] = str(2 * int(number[idx]))[-1]
            idx += 1
        
    return int("".join(number[::-1]))


def ile(digits_n, digit):
    c = 0
    lo = 10 ** (digits_n - 1)
    if digits_n == 1: lo -= 1
    up = 10 ** digits_n
    for n in range(lo, up):
        if str(digit) in str(n):
            c += 1
    return c
        

