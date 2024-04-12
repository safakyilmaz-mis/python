import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

scr = Screen()

scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("My snake game")
scr.tracer(0)  # stop the screen and animation

snake = Snake()
food = Food()
scoreboard = Scoreboard()

scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")

play_on = True
while play_on:
    scr.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        scoreboard.text()
        snake.extend()
        food.refresh()

    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        play_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:-1:1]:
        if snake.head.distance(segment) < 10:
            play_on = False
            scoreboard.game_over()


scr.exitonclick()
