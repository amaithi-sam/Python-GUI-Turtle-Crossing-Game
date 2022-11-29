from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(0, 260)
        self.scores = -1
        self.update_score()

    def update_score(self):
        self.scores += 1
        self.clear()
        self.write(f" Score {self.scores}", False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over..!", False, align="center", font=FONT)
