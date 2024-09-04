from turtle import Turtle

STARTING_POSITION = (0, -260)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 260


class Player(Turtle):
    def __init__(
        self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True
    ) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.start_position()
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def start_position(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False