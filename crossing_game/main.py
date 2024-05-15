import time
from turtle import Screen, onkey
from car_manager import carManager
from player import Player
from scoreboard import Scoreboard

SLEEP_TIME = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
car_manager = carManager()
score = Scoreboard()
num_of_car = []
screen.listen()

onkey(player.go_up, "w")

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(SLEEP_TIME)
    car_manager.new_car()
    car_manager.move()
    for car in car_manager.newCarList:
        if player.distance(car) < 20:
            player.goto(0, -280)
            car_manager.game_over()
            score.game_over()
            SLEEP_TIME = 0.1
            game_is_on = False
        if player.ycor() > 290:
            score.level_up()
            player.goto(0, -280)
            SLEEP_TIME /= 2

screen.exitonclick()
