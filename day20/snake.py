from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:
    def __init__(self) -> None:
        self.segments = list()
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x_pos = 0
        for square_index in range(3):
            new_square = Turtle(shape="square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(x_pos, 0)
            x_pos -= MOVE_DISTANCE
            self.segments.append(new_square)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
