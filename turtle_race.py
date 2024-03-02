from turtle import Turtle, Screen
import random

is_game_started = False

scr = Screen()
y_location = [100, 50, 0, -50, -100]
trt_colors = ["red", "blue", "yellow", "black", "green"]
all_turtle = []

scr.setup(width=500, height=400)
user_bet = scr.textinput(title="make your bet:", prompt="Which turtle will win the race? (enter a color): ")

for i in range(0, 5):
    trt = Turtle()
    trt.color(trt_colors[i])
    trt.penup()
    trt.shape("turtle")
    trt.goto(x=-230, y=y_location[i])
    all_turtle.append(trt)

if user_bet:
    is_game_started = True
while is_game_started:
    for a in all_turtle:
        speed = random.randint(0, 10)
        a.forward(speed)
        if a.xcor() > 230:
            if user_bet == a.pencolor():
                print(f"You won. {a.pencolor()} color won")
            else:
                print(f"You lose. {a.pencolor()} color won")
            is_game_started = False


scr.exitonclick()
