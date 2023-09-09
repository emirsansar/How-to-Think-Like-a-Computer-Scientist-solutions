#Add some new key bindings to the first sample program:
#Pressing keys R, G or B should change tess’ color to Red, Green or Blue.
#Pressing keys + or - should increase or decrease the width of tess’ pen. Ensure that the pen size stays between 1 and 20 (inclusive).
#Handle some other keys to change some attributes of tess, or attributes of the window, or to give her new behaviour that can be controlled from the keyboard.

import turtle

turtle.setup(500,500)
wn = turtle.Screen()
wn.title("Handling keypresses!")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
Pensize = 1
tess.pensize(Pensize)


def h1():
   tess.forward(30)
def h2():
   tess.left(45)
def h3():
   tess.right(45)
def h4():
    wn.bye()

def color1():
    tess.color("red")
def color2():
    tess.color("green")
def color3():
    tess.color("blue")

def h7():
    global Pensize
    Pensize = Pensize + 1
    if Pensize > 20:
        Pensize = 20
    tess.pensize(Pensize)

def h8():
    global Pensize
    Pensize = Pensize - 1
    if Pensize < 1:
        Pensize = 1
    tess.pensize(Pensize)

wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")

wn.onkey(color1, "r")
wn.onkey(color2, "g")
wn.onkey(color3, "b")

wn.onkey(h7(), "o")
wn.onkey(h8(), "l")

wn.listen()
wn.mainloop()