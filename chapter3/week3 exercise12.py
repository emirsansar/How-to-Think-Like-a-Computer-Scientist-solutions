#Write a program to draw a face of a clock that looks something like this:

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
turtle = turtle.Turtle()
turtle.shape("turtle")
turtle.color("darkblue")

turtle.stamp()

for i in range(12):
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    turtle.forward(15)
    turtle.penup()
    turtle.forward(15)
    turtle.stamp()
    turtle.back(130)
    turtle.left(30)

wn.mainloop()