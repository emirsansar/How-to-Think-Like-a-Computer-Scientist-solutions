#Write a void (non-fruitful) function to draw a square. Use it in a program to draw the image shown below. Assume each side is 20 units.
import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("pink")
tess.pensize(3)

def draw_squares(t):
    for i in range(5):
        for i in range(4):
            t.forward(20)
            t.left(90)
        t.penup()
        t.forward(40)
        t.pendown()

draw_squares(tess)

wn.mainloop()