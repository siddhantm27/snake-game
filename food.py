import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(0.5)
        self.speed("fastest")

        self.refresh()

    def select_position(self):
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        rand_position = (x, y)
        return rand_position

    def refresh(self):
        self.goto(self.select_position())