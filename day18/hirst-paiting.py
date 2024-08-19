from turtle import Turtle, Screen, colormode
from random import randint


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


tim = Turtle()
colormode(255)
tim.speed(0)
tim.penup()
tim.hideturtle()

y_pos = -250
tim.setpos(-300, y_pos)

for _ in range(10):
    for _ in range(10):
        tim.dot(25, random_color())
        tim.fd(50)
    y_pos += 50
    tim.setpos(-300, y_pos)

screen = Screen()
screen.exitonclick()
