from turtle import Turtle, Screen
from time import sleep
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
car_manager = CarManager()
# scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

screen.exitonclick()
