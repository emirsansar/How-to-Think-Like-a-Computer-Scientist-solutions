#Write a void function to draw a star, where the length of each side is 100 units. (Hint: You should turn the turtle by 144 degrees at each point.)

import turtle

wn=turtle.Screen()
tess=turtle.Turtle()

def draw_star(t,sz):
    t.right(72)

    for i in range(5):
        t.forward(sz)
        t.right(144)

draw_star(tess,50)

wn.mainloop()