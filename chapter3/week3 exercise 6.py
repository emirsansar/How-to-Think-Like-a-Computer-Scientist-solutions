import turtle

wn = turtle.Screen()
turtle = turtle.Turtle()
turtle.shape("turtle")

for i in range(3): #triangle
    turtle.forward(60)
    turtle.left(120)

for i in range(4): #square
    turtle.forward(60)
    turtle.left(90)

for i in range(6): #hexagon
    turtle.forward(60)
    turtle.left(60)

for i in range(9): #octagon
    turtle.forward(60)
    turtle.left(40)

wn.mainloop()