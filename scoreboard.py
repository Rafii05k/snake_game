from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(-10, 265)
        self.write(f"score: {self.score}", align="center", font=("Arial", 23, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align="center", font=("Arial", 23, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"score: {self.score}", align="center", font=("Arial", 23, "normal"))
