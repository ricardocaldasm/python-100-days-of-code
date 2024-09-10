from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 24, "bold")


class Scoreboard(Turtle):

    def __init__(
        self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True
    ) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        with open(r"day24\data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} | High Score: {self.high_score}",
            align=ALIGN,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(r"day24\data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
