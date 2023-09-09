#Write a void function draw_equitriangle(t, sz) which calls draw_poly from the previous question to have its turtle draw a equilateral triangle.

import turtle

wn=turtle.Screen()
wn.bgcolor("lightgreen")
tess=turtle.Turtle()
tess.color("pink")
tess.pensize(3)

def draw_equitriangle(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(120)

draw_equitriangle(tess,3,40)

wn.mainloop()