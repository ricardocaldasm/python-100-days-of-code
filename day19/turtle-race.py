from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
all_turtles = list()

def finish_line_race():
    finish_line = Turtle()
    finish_line.speed(0)
    finish_line.hideturtle()
    finish_line.penup()
    finish_line.goto(220,200)
    finish_line.pendown()
    finish_line.goto(220,-200)

finish_line_race()

y_pos = 150

for turtle_index in range(7):
    new_turtle = Turtle(shape="turtle")  # instance | they can have different attributes
    # turtle_2 = Turtle(shape="turtle")  # instance
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-200, y_pos)
    y_pos -= 50
    all_turtles.append(new_turtle)
    new_turtle.speed(0)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 200:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner.")
            else:
                 print(f"You've lost! The {winning_color} is the winner.")
        rand_distance = randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()
