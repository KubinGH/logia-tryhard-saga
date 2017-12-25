from turtle import *

def square(a, color):
    fillcolor(color)
    begin_fill()
    for i in range(4):
        forward(a)
        right(90)
    end_fill()

def colors(char):
    fix = int(ord(char) > ord("I")) + int(ord(char) > ord("U"))
    char = chr(ord(char) - fix)
    yield from ("blue" if int(b) else "yellow" for b in bin(ord(char)-ord("A"))[2:].zfill(5)[::-1])

def szyfruj(string):
    a = 400 / 5
    if len(string) * a > 794:
        a = 700 / len(string)
    pu(); back(len(string) / 2 * a); right(90)
    back(2.5 * a); left(90); pd()
    for char in string:
        start = pos()
        for color in colors(char):
            square(a, color)
            pu(); right(90); forward(a); left(90); pd()
        pu(); goto(start); forward(a); pd()


if __name__ == "__main__":
    import string
    tracer(0)
    szyfruj(string.ascii_uppercase)    
    exitonclick()
