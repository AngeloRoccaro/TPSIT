import turtle

#loop
while True:
    win.update()

#background
win = turtle.Screen()
win.title("snake")
win.bgcolor("black")
win.setup(width=600,height=600)
win.tracer(0)

#snake
head = turtle.Turtle()
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 100)
head.direction = "stop"
head.speed(0)