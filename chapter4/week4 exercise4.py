#Draw this pretty pattern.
import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)
tess.speed(10)

def draw_square(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
    t.right(18)

for i in range(20):
    draw_square(tess,50)

wn.mainloop()