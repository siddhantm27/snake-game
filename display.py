from turtle import Turtle,Screen

class Display():

    def __init__(self):





    def score(self,score):
        t_score = Turtle()
        t_score.color("white")
        t_score.penup()
        t_score.goto(0,230)
        t_score.pendown()
        t_score.write(f"Score: {score}")
