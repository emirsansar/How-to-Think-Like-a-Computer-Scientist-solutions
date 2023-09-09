#Set up a list of pairs so that the turtle draws a house with a cross through the centre, as show here.
# This should be done without going over any of the lines / edges more than once, and without lifting your pen.

import math
import turtle


degree_and_step_list = [(180, 30), (-135, 30*math.sqrt(2)), (135, 30), (-135, 15*math.sqrt(2) ), (-90, 15*math.sqrt(2)), (-45,30), (-135, 30*math.sqrt(2)), (135,30)]

wn = turtle.Screen()
turtle = turtle.Turtle()
turtle.shape("turtle")
turtle.speed(5)

for (degree, step) in degree_and_step_list:
    turtle.left(degree)
    turtle.forward(step)

wn.mainloop()