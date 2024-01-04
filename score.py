# Score turtle
from turtle import Turtle


class Score:

    def __init__(self):
        self.score_t = Turtle()
        self.score_t.color("white")
        self.score_t.penup()
        self.score_t.goto(x=0, y=230)
        self.score_t.pendown()
        self.score_t.ht()
        self.current_score = 0
        with open("high_score.txt") as highscore:
            self.high_score = int(highscore.read())

    def add_score(self):
        self.current_score += 1

    def display_score(self):
        self.score_t.clear()
        self.score_t.write(f"Score: {self.current_score} High Score: {self.high_score}", align="center")

    def reset_score(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.current_score}")
        self.current_score = 0

    # def game_over(self):
    #     self.score_t.clear()
    #     self.score_t = Turtle()
    #     self.score_t.color("white")
    #     self.score_t.write("Game Over!", align="center")
    #     self.score_t.penup()
    #     self.score_t.goto(x=0, y=230)
    #     self.score_t.pendown()
    #     self.score_t.write(f"Final Score: {self.current_score}", align="center")
    #     self.score_t.ht()
