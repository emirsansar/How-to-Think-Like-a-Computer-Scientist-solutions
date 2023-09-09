#Extend your program above. Draw five stars, but between each, pick up the pen, move forward by 350 units, turn right by 144, put the pen down, and draw the next star.

import turtle

wn=turtle.Screen()
wn.bgcolor("lightgreen")
tess=turtle.Turtle()
tess.color("pink")
tess.pensize(3)
tess.speed(10)

def draw_star(t):
    t.right(72)
    for i in range(5):
        t.forward(50)
        t.right(144)

def draw_five_star(t):
    for i in range(5):
        draw_star(t)
        t.penup()
        t.right(144)
        t.forward(100)
        t.pendown()

draw_five_star(tess)

wn.mainloop()