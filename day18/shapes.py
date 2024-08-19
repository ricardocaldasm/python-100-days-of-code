from turtle import Turtle, Screen

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        for _ in range (10):
            tim.forward(5)
            tim.penup()
            tim.forward(5)
            tim.pendown()
        tim.right(angle)

tim = Turtle()  # object
tim.shape("turtle")
tim.color("green")

for shape_side_n in range(3,11):
    draw_shape(shape_side_n)

screen = Screen()  # object
screen.exitonclick()
