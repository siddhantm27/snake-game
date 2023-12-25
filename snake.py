from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_body()
        self.head = self.segments[0]

    def create_body(self):
        for position in POSITIONS:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        for n in range(len(self.segments) - 1, 0, -1):
            next_x = self.segments[n - 1].xcor()
            next_y = self.segments[n - 1].ycor()
            self.segments[n].penup()
            self.segments[n].goto(next_x, next_y)
        self.head.forward(20)

    def turn_left(self):
        self.head.left(90)

    def turn_right(self):
        self.head.right(90)
