import turtle
import pandas
import os
#you should install the pandas module to work on the pandas projects

screen = turtle.Screen()
screen.title("U.S. Guess Game")
image = os.path.join(os.path.dirname(__file__),"blank_states_img.gif")
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv(os.path.join(os.path.dirname(__file__),"50_states.csv"))
state = states["state"].tolist()
x_loc_states = states["x"].tolist()
y_loc_states = states["y"].tolist()

gameison = True
counter = 0
correct_states = []

while gameison:
    answer = screen.textinput(f"{counter}/50 States correct", "Enter your guess:").title()

    if answer not in state and not "q":
        answer = screen.textinput(f"{counter}/50 States correct", "Enter your guess:").title()

    if answer in state:
        if answer not in correct_states:
            counter += 1
        turtle4states = turtle.Turtle()
        turtle4states.penup()
        turtle4states.hideturtle()
        turtle4states.goto(x_loc_states[state.index(answer)], y_loc_states[state.index(answer)])
        turtle4states.write(answer, False, "center")
        correct_states.append(answer)

    if len(state) == 0:
        turtle4states = turtle.Turtle()
        turtle4states.write("You Know all The States. Congratulations!", False, "center", ("Arial", 28, "normal"))


    if answer == "Exit":
        missing_states = []
        for i in state:
            if i not in correct_states:
                missing_states.append(i)
        gameison = False
        pandas.DataFrame(missing_states).to_csv(os.path.join(os.path.dirname(__file__), "Missed_States.csv"))
        break
