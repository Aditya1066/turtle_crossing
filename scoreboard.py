from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.ht()
        self.goto(-280, 250)
        self.write(f"Level:{self.level}", align="left", font=FONT)

    def next_level(self):
        self.level += 1

    def refresh_scoreboard(self):
        self.clear()
        self.write(f"Level:{self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(-50, 0)
        self.write("Game Over", font=FONT)
