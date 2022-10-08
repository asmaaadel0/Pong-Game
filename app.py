import turtle

wind = turtle.Screen() #initialize screen
wind.title("Ping Pong") #set the title of the window
wind.bgcolor("black") #set background color
wind.setup(width=800, height=600) #set width, height
wind.tracer(0) #Prevents the screen from updating

#Racket1
racket1 = turtle.Turtle()
racket1.speed(0)
racket1.shape("square")
racket1.color("green")
racket1.shapesize(stretch_wid=5, stretch_len=1)
racket1.penup()
racket1.goto(-350, 0)

#Racket2
racket2 = turtle.Turtle()
racket2.speed(0)
racket2.shape("square")
racket2.color("blue")
racket2.shapesize(stretch_wid=5, stretch_len=1)
racket2.penup()
racket2.goto(350, 0)

#main game loop
while True:
    wind.update() #updates the screen everytime





