from turtle import Turtle, Screen

tim = Turtle()  # object

tim.shape("turtle")
tim.color("green")
for _ in range(4):
    tim.forward(100)
    tim.right(90)

screen = Screen()  # object
screen.exitonclick()
