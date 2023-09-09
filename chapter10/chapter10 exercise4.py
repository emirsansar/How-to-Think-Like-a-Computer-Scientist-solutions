#Now that you’ve got a traffic light program with different turtles for each light, perhaps the visibility / invisibility trick wasn’t such a great idea. If we watch traffic lights, they turn on and off — but when they’re off they are still there, perhaps just a darker color.
# Modify the program now so that the lights don’t disappear: they are either on, or off. But when they’re off, they’re still visible.

import turtle           # Tess becomes a traffic light.

turtle.setup(600,600)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.speed(10)

tess_red = turtle.Turtle()
tess_red.color("dark red")
tess_red.shape("circle")
tess_red.shapesize(3)
tess_red.penup()

tess_orange = turtle.Turtle()
tess_orange.color("sienna")
tess_orange.shape("circle")
tess_orange.shapesize(3)
tess_orange.penup()

tess_green = turtle.Turtle()
tess_green.color("light green")
tess_green.shape("circle")
tess_green.shapesize(3)
tess_green.penup()


def draw_housing():
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()

tess_green.goto(40,50)          # ışıkları yerlerine gönderir ve iz bıraktırır.
tess_green.pendown()
tess_green.shape()
tess_orange.goto(40,120)
tess_orange.pendown()
tess_green.shape()
tess_red.goto(40,190)
tess_orange.pendown()
tess_green.shape()

state_num = 0

def advance_state_machine():
    global state_num
    if state_num == 0:       #      yeşil söner, turuncu yanar
        tess_green.color("dark green")
        tess_orange.color("orange")
        state_num = 1
    elif state_num == 1:     #      turuncu söner, kırmızı yanar.
        tess_orange.color("sienna")
        tess_red.color("red")
        state_num = 2
    else:                    # kırmızı söner, yeşil yanar.
        tess_red.color("dark red")
        tess_green.color("light green")

        state_num = 0
    wn.ontimer(advance_state_machine, 1000)  # 1 saniye'de bir state_num değişir.

wn.ontimer(advance_state_machine, 1000)  # ilk yeşil ışıkta da 1 saniye bekler.

wn.listen()
wn.mainloop()