#Your traffic light controller program has been patented, and you’re about to become seriously rich. But your new client needs a change.
# They want four states in their state machine: Green, then Green and Orange together, then Orange only, and then Red.
# , they want different times spent in each state. The machine should spend 3 seconds in the Green state, followed by one second in the Green+Orange state,
# then one second in the Orange state, and then 2 seconds in the Red state. Change the logic in the state machine.

import turtle           # Tess becomes a traffic light.

turtle.setup(600,600)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("light green")
tess = turtle.Turtle()
tess.speed(10)

tess_red = turtle.Turtle()
tess_red.hideturtle()
tess_red.color("dark red")
tess_red.shape("circle")
tess_red.shapesize(3)
tess_red.penup()

tess_orange = turtle.Turtle()
tess_orange.hideturtle()
tess_orange.color("sienna")
tess_orange.shape("circle")
tess_orange.shapesize(3)
tess_orange.penup()

tess_green = turtle.Turtle()
tess_green.hideturtle()
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
tess.hideturtle()

tess_green.goto(40,50)          # ışıkları yerlerine gönderir ve iz bıraktırır.
tess_green.pendown()
tess_green.fillcolor()
tess_orange.goto(40,120)
tess_orange.pendown()
tess_green.fillcolor()
tess_red.goto(40,190)
tess_orange.pendown()
tess_green.fillcolor()
tess_green.showturtle()
tess_orange.showturtle()
tess_red.showturtle()

state_num = 0

def advance_state_machine():
    global state_num

    if state_num == 0:
        tess_orange.color("orange")
        tess_green.color("dark green")
        state_num = 1
        gecen_zaman = 1000
    elif state_num == 1:
        tess_orange.color("sienna")
        tess_red.color("red")
        state_num = 2
        gecen_zaman = 2000
    elif state_num == 2:
        tess_red.color("dark red")
        tess_green.color("light green")
        gecen_zaman = 3000
        state_num = 3
    elif state_num == 3:
        tess_orange.color("orange")
        gecen_zaman = 1000
        state_num = 0

    wn.ontimer(advance_state_machine, gecen_zaman)      # gecen zaman kadar state_num'a göre ışıkları yakar.

wn.ontimer(advance_state_machine, 1000)  # ilk 1 saniye bekler

wn.listen()
wn.mainloop()