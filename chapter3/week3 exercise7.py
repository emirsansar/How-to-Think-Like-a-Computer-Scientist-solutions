#A drunk pirate makes a random turn and then takes 100 steps forward, makes another random turn, takes another 100 steps, turns another random amount, etc.
# A social science student records the angle of each turn before the next 100 steps are taken. Her experimental data is [160, -43, 270, -97, -43, 200, -940, 17, -86].
# Use a turtle to draw the path taken by our drunk friend

import turtle

degree_list = [160, -43, 270, -97, -43, 200, -940, 17, -86]

wn = turtle.Screen()
wn.bgcolor("cyan")
turtle = turtle.Turtle()
turtle.shape("turtle")

for i in degree_list:
    turtle.forward(100)
    turtle.left(i)

wn.mainloop()