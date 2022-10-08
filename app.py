from asyncore import write
from ctypes import alignment
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
ball.dx = .5
ball.dy = .5

# score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player1: 0 Player 2: 0", align="center",
            font=("Courier", 24, "normal"))

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

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("Player1: {} Player 2: {}".format(score1, score2), align="center",
                    font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score.clear()
        score2 += 1
        score.write("Player1: {} Player 2: {}".format(score1, score2), align="center",
                    font=("Courier", 24, "normal"))

    # Racket and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < racket2.ycor()+40 and ball.ycor() > racket2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < racket1.ycor()+40 and ball.ycor() > racket1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
