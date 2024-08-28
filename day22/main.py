from turtle import Screen
from paddles import Paddles

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0) # when you turn off animation, you have to manually update the screen and refresh it

paddles = Paddles()

screen.listen()
screen.onkey(paddles.go_up, "w")
screen.onkey(paddles.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()
