from turtle import Turtle, Screen
from food import Food
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

    tail_hit = snake.tail_check()
    wall_hit = snake.wall_check()

    if tail_hit or wall_hit:
        snake.new_game()
        snake.head = snake.segments[0]
        score.reset_score()
        time.sleep(1)

    if snake.head.distance(food) <= 15:
        food.refresh()
        snake.add_segment()
        score.add_score()

screen.exitonclick()
