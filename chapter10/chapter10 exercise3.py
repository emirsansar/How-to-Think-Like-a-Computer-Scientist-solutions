import turtle           # Tess becomes a traffic light.

turtle.setup(600,600)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.speed(10)

tess_red = turtle.Turtle()              # kırmızı sabit ışık için
tess_red.hideturtle()
tess_red.color("red")
tess_red.shape("circle")
tess_red.shapesize(3)
tess_red.penup()

tess_orange = turtle.Turtle()           # turuncu sabit ışık için
tess_orange.hideturtle()
tess_orange.color("orange")
tess_orange.shape("circle")
tess_orange.shapesize(3)
tess_orange.penup()

tess_green = turtle.Turtle()            # yeşil sabit ışık için
tess_green.hideturtle()
tess_green.color("green")
tess_green.shape("circle")
tess_green.shapesize(3)
tess_green.penup()

tess_green.goto(140,50)         # ışıkları yerlerine gönderir.
tess_green.pendown()
tess_orange.goto(140,120)
tess_orange.pendown()
tess_red.goto(140,190)
tess_orange.pendown()


def draw_housing():             # ilk tabelayı çizer.
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

def draw_housing2():                # 2. tabelayı çizer
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.penup()
    tess.forward(100)
    tess.pendown()
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()
draw_housing2()

tess.penup()                # ilk ışık tabelası için tess'i ilk tabelaya gönderir ve yeşil ışık yapar.
tess.goto(0,0)
tess.forward(40)
tess.left(90)
tess.forward(50)
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

tess_green.showturtle()

state_num = 0

def advance_state_machine():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        tess_green.hideturtle()
        tess_orange.showturtle()
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1:     # Transition from state 1 to state 2
        tess_orange.hideturtle()
        tess_red.showturtle()
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else:                    # Transition from state 2 to state 0
        tess_red.hideturtle()
        tess_green.showturtle()
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0
    wn.ontimer(advance_state_machine, 1000)  # 1 saniye'de bir state_num değişir.

wn.ontimer(advance_state_machine, 1000)  # ilk yeşil ışıkta da 1 saniye bekler.

wn.listen()
wn.mainloop()