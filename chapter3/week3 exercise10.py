#At the interactive prompt, anticipate what each of the following lines will do, and then record what happens.
# Score yourself, giving yourself one point for each one you anticipate correctly:


import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
tess.right(90)  # turn 90 degree
tess.left(3600) # stays where it is
tess.right(-90) # returns to where it started
tess.speed(10)  # speeds or slows
tess.left(3600) # stays where it is
tess.speed(0)   # stop
tess.left(3645) # turn 45 degree
tess.forward(-100)  # moves 100 units

wn.mainloop()
