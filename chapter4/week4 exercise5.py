#The two spirals in this picture differ only by the turn angle. Draw both.
import turtle

wn=turtle.Screen()
wn.bgcolor("lightgreen")
tess=turtle.Turtle()
tess.pensize(1)
tess.color("pink")
tess.speed(10)

def draw_spiral(t,sz):
    for i in range(90):
        t.right(90)  # If we increase the angle, we can draw the other figure.
        t.forward(sz)
        sz += 5

draw_spiral(tess,5)

wn.mainloop()