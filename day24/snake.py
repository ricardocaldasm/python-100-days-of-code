from turtle import Turtle

STARTING_POSITION = [(0, 0), (0, -20), (0, -40)]
MOVE_DISTANCE = 20


class Snake(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.segments = list()
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        self.shape("square")
        self.color("white")
        self.goto(position)
        # new_segment = Turtle(shape="square")
        # new_segment.color("white")
        # new_segment.penup()
        # new_segment.goto(position)
        # self.segments.append(new_segment)
