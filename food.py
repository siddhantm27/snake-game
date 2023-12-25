# def check_food(snake, food):
#     if abs(snake.xcor() - food.xcor()) < 10 and abs(snake.ycor() - food.ycor()) < 10:
#         return True
#     else:
#         return False

# def create_food():
#     food = Turtle()
#     food.shape("circle")
#     food.color("red")
#     food.shapesize(0.5, 0.5)
#     x = random.randint(0, 230)
#     y = random.randint(0, 230)
#     food.penup()
#     food.speed("fastest")
#     food.goto(x, 0)
#     return food

import random
from turtle import Turtle


class Food:

    def __init__(self):
        t = Turtle("circle")
        t.color("green")
        t.penup()
        self.food = t

        self.food.goto(self.select_position())

    def select_position(self):
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        rand_position = (x, y)
        return rand_position
