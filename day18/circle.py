from turtle import Turtle, Screen, colormode
from random import randint

tim = Turtle()
tim.speed(0)

n = 0
increase = 5
number_of_circles = int(360 / increase) + 1
for _ in range(number_of_circles):
    tim.circle(100)
    tim.setheading(n)
    n += increase


screen = Screen()  # object
screen.exitonclick()
