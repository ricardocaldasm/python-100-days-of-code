from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]

y_pos = 150

for turtle_index in range(7):
    turtle_1 = Turtle(shape="turtle")  # instance | they can have different attributes
    # turtle_2 = Turtle(shape="turtle")  # instance
    turtle_1.penup()
    turtle_1.color(colors[turtle_index])
    turtle_1.goto(-200, y_pos)
    y_pos -= 50

screen.exitonclick()
