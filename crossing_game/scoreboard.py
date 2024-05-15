from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("Black")
        self.hideturtle()
        self.penup()
        self.goto(-10, 240)
        self.write(f"Score:{self.score}", False, ALIGNMENT, FONT)

    def level_up(self):
        self.clear()
        self.score += 1
        self.write(f"Score:{self.score}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(-10, 0)
        self.write(f"Game Over", False, ALIGNMENT, FONT)
