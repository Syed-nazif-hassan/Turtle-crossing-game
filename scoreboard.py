from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.score_board()

    def score_board(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(-260, 250)
        self.write(arg=f"level {self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align="center", font=FONT)
