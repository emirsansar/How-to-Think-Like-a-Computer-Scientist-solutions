#Revisit the drunk pirate problem from the exercises in chapter 3. This time, the drunk pirate makes a turn, and then takes some steps forward, and repeats this.
# Our social science student now records pairs of data: the angle of each turn, and the number of steps taken after the turn.
# Her experimental data is [(160, 20), (-43, 10), (270, 8), (-43, 12)]. Use a turtle to draw the path taken by our drunk friend.

import turtle

degree_and_step_list = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

wn = turtle.Screen()
wn.bgcolor("cyan")
turtle = turtle.Turtle()
turtle.shape("turtle")

for (degree, step) in degree_and_step_list:
    turtle.left(degree)
    turtle.forward(step)

wn.mainloop()