import time
from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment_list = []
        self.x_pos = 0
        self.create_snake()
        self.head = self.segment_list[0]
        self.is_moved = False

    def create_snake(self):
        for i in range(3):
            segment = Turtle(shape='square')
            self.segment_list.append(segment)
            segment.color('white')
            segment.penup()
            segment.speed('fastest')
            segment.setposition(self.x_pos, 0)
            self.x_pos -= 20

    def move(self):
        for i in range(len(self.segment_list) - 1, 0, -1):
            new_x = self.segment_list[i - 1].xcor()
            new_y = self.segment_list[i - 1].ycor()
            self.segment_list[i].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)
        self.is_moved = True

    def up(self):
        if self.head.heading() != DOWN and self.is_moved == True:
            self.head.seth(UP)
            self.is_moved = False

    def down(self):
        if self.head.heading() != UP and self.is_moved == True:
            self.head.seth(DOWN)
            self.is_moved = False

    def left(self):
        if self.head.heading() != RIGHT and self.is_moved == True:
            self.head.seth(LEFT)
            self.is_moved = False

    def right(self):
        if self.head.heading() != LEFT and self.is_moved == True:
            self.head.seth(RIGHT)
            self.is_moved = False

    def increase_snake(self):
        segment = Turtle(shape='square')
        self.segment_list.append(segment)
        segment.color('white')
        segment.penup()
