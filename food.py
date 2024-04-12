from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape()
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("aqua")
        self.shape("circle")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        food_loc_x = random.randint(-280, 280)
        food_loc_y = random.randint(-280, 280)
        self.goto(food_loc_x, food_loc_y)
