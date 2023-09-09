#Write a program to draw this. Assume the innermost square is 20 units per side, and each successive square is 20 units bigger, per side, than the one inside it.
import turtle

wn=turtle.Screen()
wn.bgcolor("lightgreen")
tess=turtle.Turtle()
tess.color("pink")
tess.pensize(3)

def draw_squares(t,sz):
    for i in range(5):
        for i in range(4):
            t.forward(sz)
            t.left(90)
        t.penup()
        t.goto(-(sz / 2), -(sz / 2))
        sz += 20
        t.pendown()

draw_squares(tess,20)

wn.mainloop()