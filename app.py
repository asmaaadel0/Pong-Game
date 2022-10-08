import turtle

wind = turtle.Screen()  # initialize screen
wind.title("Ping Pong")  # set the title of the window
wind.bgcolor("black")  # set background color
wind.setup(width=800, height=600)  # set width, height
wind.tracer(0)  # Prevents the screen from updating

# Racket1
racket1 = turtle.Turtle()
racket1.speed(0)
racket1.shape("square")
racket1.color("green")
racket1.shapesize(stretch_wid=5, stretch_len=1)
racket1.penup()
racket1.goto(-350, 0)

# Racket2
racket2 = turtle.Turtle()  # initialize object
racket2.speed(0)  # set speed of the ainmation
racket2.shape("square")  # set shape object
racket2.color("blue")  # set color object
racket2.shapesize(stretch_wid=5, stretch_len=1)  # stretches the shape
racket2.penup()  # stops the object frowm drawing lines
racket2.goto(350, 0)  # set object position

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# functions


def racket1_up():
    y = racket1.ycor()
    y += 20
    racket1.sety(y)


def racket1_down():
    y = racket1.ycor()
    y -= 20
    racket1.sety(y)

def racket2_up():
    y = racket2.ycor()
    y += 20
    racket2.sety(y)


def racket2_down():
    y = racket2.ycor()
    y -= 20
    racket2.sety(y)    


# def racket1_up():
#     y = racket2.ycor()
#     y += 20
#     racket2.sety(y)


# keyboard binding
wind.listen()
wind.onkeypress(racket1_up, "w")
wind.onkeypress(racket1_down, "s")

wind.onkeypress(racket2_up, "Up")
wind.onkeypress(racket2_down, "Down")


# main game loop
while True:
    wind.update()  # updates the screen everytime
