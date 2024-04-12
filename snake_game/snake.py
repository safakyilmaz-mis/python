import turtle
from turtle import Screen, Turtle

SNAKE_LOCATIONS = [(40, 0), (20, 0), (0, 0)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

scr = Screen()


class Snake:
    # init arabayi calistiran anahtar gibi dusun her sey burada calistiriliyor OOP'de
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in SNAKE_LOCATIONS:
            self.add_segment(i)

    # arabanin motoru self.segments[0] bu yuzden turtle yerine bu objecyi ekledik

    def add_segment(self,  pos):
        trt = Turtle()
        trt.penup()
        trt.goto(pos)
        trt.color("white")
        trt.shape("square")
        trt.pensize(20)
        self.segments.append(trt)
        scr.update()  # after these steps play the animations

    def extend(self):
        self.add_segment(self.segments[-1].position())
        #position metodu turtle sinifindan geliyor.

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        scr.listen()
        self.head.forward(MOVE_FORWARD)
