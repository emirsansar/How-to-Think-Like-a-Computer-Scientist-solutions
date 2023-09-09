# Write a program to draw a shape like this: a star

import turtle

wn = turtle.Screen()
wn.title("Star")
turtle = turtle.Turtle()
turtle.pensize(5)
turtle.hideturtle()

"I found the degrees of star on the Internet."
turtle.left(36)

for i in range(5):
    turtle.forward(100)
    turtle.left(144)

wn.mainloop()