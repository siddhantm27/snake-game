# Score turtle
from turtle import Turtle


class Score:

    def __init__(self):
        self.current_score = 0
        self.score_t = Turtle()

    def add_score(self):
        self.current_score += 1

    def display_score(self):
        self.score_t.clear()
        self.score_t = Turtle()
        self.score_t.color("white")
        self.score_t.penup()
        self.score_t.goto(x=0, y=230)
        self.score_t.pendown()
        self.score_t.write(f"Score: {self.current_score}", align="center")
        self.score_t.ht()

    def game_over(self):
        self.score_t.clear()
        self.score_t = Turtle()
        self.score_t.color("white")
        self.score_t.write("Game Over!", align="center")
        self.score_t.penup()
        self.score_t.goto(x=0, y=230)
        self.score_t.pendown()
        self.score_t.write(f"Final Score: {self.current_score}", align="center")
        self.score_t.ht()
