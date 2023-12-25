from turtle import Turtle, Screen
import math
import time

screen = Screen()


def add_segment(segments):
    t = Turtle()
    t.shape("square")
    t.color("white")
    t.penup()
    prev_t = segments[-1]
    prev_angle = prev_t.heading()
    x = prev_t.xcor()
    y = prev_t.ycor()
    new_x = x - 20 * math.cos(prev_angle)
    new_y = y - 20 * math.sin(prev_angle)

    t.goto(x=new_x, y=new_y)
    segments.append(t)
    time.sleep(0.1)
    screen.update()
    return segments
