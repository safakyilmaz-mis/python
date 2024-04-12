from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("aqua")
        self.penup()
        self.hideturtle()
        self.text()

    def text(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.write(f"Game Over.", align=ALIGNMENT, font=FONT)
