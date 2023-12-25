from turtle import Turtle
import math

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_body()
        self.head = self.segments[0]
        self.tail_hit = False

    def create_body(self):
        for position in POSITIONS:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def add_segment(self):
        segment = Turtle("square")
        segment.color("white")
        segment.speed("fastest")
        segment.penup()
        prev_t = self.segments[-1]
        prev_angle = prev_t.heading()
        x = prev_t.xcor()
        y = prev_t.ycor()
        new_x = x - 20 * math.cos(prev_angle)
        new_y = y - 20 * math.sin(prev_angle)
        segment.goto(new_x, new_y)
        self.segments.append(segment)

    def move(self):
        for n in range(len(self.segments) - 1, 0, -1):
            next_x = self.segments[n - 1].xcor()
            next_y = self.segments[n - 1].ycor()
            self.segments[n].penup()
            self.segments[n].goto(next_x, next_y)
        self.head.forward(20)

    def wall_check(self):
        x = self.head.xcor()
        y = self.head.ycor()
        if self.head.heading() == 0 and x >= 240:
            return True
        elif self.head.heading() == 90 and y >= 240:
            return True
        elif self.head.heading() == 180 and x <= -240:
            return True
        elif self.head.heading() == 270 and y <= -240:
            return True
        else:
            return False

    def tail_check(self):
        for n in range(len(self.segments) - 1, 1, -1):
            if self.head.distance(self.segments[n]) < 20:
                self.tail_hit = True
                break

    def go_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def go_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def go_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def go_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
