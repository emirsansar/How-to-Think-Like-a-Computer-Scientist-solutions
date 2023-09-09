#Modify the turtle bar chart program so that the pen is up for the small gaps between each bar.

import turtle

def draw_bar(t, height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.penup()                # i added this line for small gaps for each bar.
    t.forward(10)
    t.pendown()              # i added this line for small gaps for each bar.

wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue", "red")
tess.pensize(3)

xs = [48,117,200,240,160,260,220]
for a in xs:
    draw_bar(tess, a)

wn.mainloop()