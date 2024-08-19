from turtle import Turtle, Screen, colormode
from random import choice, randint


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


directions = [0, 90, 180, 270]

tim = Turtle()  # object
tim.pensize(2)
tim.speed(0)
colormode(255)


while True:
    tim.color(random_color())
    tim.forward(10)
    tim.setheading(choice(directions))


screen = Screen()  # object
screen.exitonclick()
