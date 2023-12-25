from turtle import Turtle, Screen
from food import Food
import math
import random
import time
from snake import Snake

screen = Screen()
screen.bgcolor("black")
screen.setup(height=500, width=500)
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkeypress(key="a", fun=snake.turn_left)
screen.onkeypress(key="d", fun=snake.turn_right)
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()


# food = create_food()
# while no_wall:
#     for segment in segments:
#         segment.penup()
#         segment.forward(20)
#     time.sleep(0.1)
#     screen.update()
#
#     first_turtle = segments[0]
#     # if check_food(first_turtle, food):
#     #     segments = add_segment(segments)
#     #     food.ht()
#     #     food = create_food()
#     x = first_turtle.xcor()
#     # turn()
#     # screen.listen()
#     # screen.onkeypress(key="a", fun=turn_left)
#     if x >= 230:
#         no_wall = False
