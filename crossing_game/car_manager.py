import random
from turtle import Turtle
from player import Player

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 100


class carManager:
    def __init__(self):
        self.newCarList = []

    def new_car(self):
        chanceOfCar = random.randint(1, 6)
        if chanceOfCar == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.turtlesize(1, 2)
            new_car.goto(320, random.randint(-250, 250))
            self.newCarList.append(new_car)

    def move(self):
        # Here i is already in newCarList, so you dont need to say like newCarList[i] or different wrong things
        # You can directly write "i".backward(number)
        for i in self.newCarList:
            i.backward(STARTING_MOVE_DISTANCE)



    def game_over(self):
        for i in self.newCarList:
            i.backward(STARTING_MOVE_DISTANCE)
