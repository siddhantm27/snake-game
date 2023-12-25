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
screen.onkeypress(key="Left", fun=snake.go_left)
screen.onkeypress(key="Right", fun=snake.go_right)
screen.onkeypress(key="Up", fun=snake.go_up)
screen.onkeypress(key="Down", fun=snake.go_down)

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) <= 15:
        food.refresh()
        snake.add_segment()

screen.exitonclick()


