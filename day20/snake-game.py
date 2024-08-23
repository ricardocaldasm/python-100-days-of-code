from turtle import Turtle, Screen
from time import sleep

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

segments = list()

x_pos = 0
for square_index in range(3):
    new_square = Turtle(shape="square")
    new_square.color("white")
    new_square.penup()
    new_square.goto(x_pos, 0)
    x_pos -= 20
    segments.append(new_square)

game_is_on = True

while game_is_on:
    screen.update()
    sleep(0.1)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

screen.exitonclick()
