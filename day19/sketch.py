from turtle import Turtle, Screen


def move_forward():
    tim.forward(20)


def move_backward():
    tim.backward(20)


def turn_left():
    tim.left(45)


def turn_right():
    tim.right(45)


def clear():
    tim.home()
    tim.clear()


tim = Turtle()
screen = Screen()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()
