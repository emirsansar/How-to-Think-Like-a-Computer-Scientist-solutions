#Modify the turtle bar chart program so that the bar for any value of 200 or more is filled with red, values between [100 and 200) are filled with yellow,
# and bars representing values less than 100 are filled with green.

import turtle

def draw_bar(t, height):
    if height>=200:
        tess.color("blue", "red")
    elif 200>height and height>=100:
        tess.color("blue", "yellow")
    else:
        tess.color("blue", "green")            # i added the lines from 7 to 12 to change the color.

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
    t.forward(10)

wn = turtle.Screen()
wn.bgcolor("grey")
tess = turtle.Turtle()
tess.pensize(3)

xs = [48,117,200,240,160,260,220]
for a in xs:
    draw_bar(tess, a)