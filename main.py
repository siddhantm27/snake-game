from turtle import Turtle, Screen
from food import Food
import math
import random
import time
from snake import Snake
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(height=500, width=500)
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkeypress(key="Left", fun=snake.go_left)
screen.onkeypress(key="Right", fun=snake.go_right)
screen.onkeypress(key="Up", fun=snake.go_up)
screen.onkeypress(key="Down", fun=snake.go_down)

game_on = True

while game_on:
    score.display_score()
    screen.update()
    time.sleep(0.1)
    snake.move()

    snake.tail_check()
    if snake.tail_hit:
        game_on = False
        score.game_over()

    if snake.head.distance(food) <= 15:
        food.refresh()
        snake.add_segment()
        score.add_score()

    wall_hit = snake.wall_check()
    if wall_hit:
        game_on = False
        score.game_over()

screen.exitonclick()
