from turtle import Turtle

COORD = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for i in COORD:
            self.add_segment(i)

    def add_segment(self,position):
            tim = Turtle()
            tim.shape("square")
            tim.color("white")
            tim.penup()
            tim.goto(position)
            self.segments.append(tim)

    def extend_l(self):
        pos=self.segments[-1].position()
        self.add_segment(pos)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.segments[0].setheading(90)

    def down(self):
        if self.head.heading()!=UP:
            self.segments[0].setheading(270)

    def right(self):
        if self.head.heading()!=LEFT:
            self.segments[0].setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(180)
