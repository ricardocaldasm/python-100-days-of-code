from time import sleep
from turtle import Turtle, Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

# screen.listen()
# screen.onkey(snake.up, "w")
# screen.onkey(snake.down, "s")
# screen.onkey(snake.left, "a")
# screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)

screen.exitonclick()