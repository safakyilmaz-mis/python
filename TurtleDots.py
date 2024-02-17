import random
import colorgram
from turtle import Turtle, Screen, colormode

trt = Turtle()
scr = Screen()

trt.hideturtle()
colors = colorgram.extract("xxx.jpg", 25) #xxx: photo's name which is in the same location with this code
rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
  
for i in range(2):
    rgb_colors.pop(0)

height_value = 0
for i in range(10):
    trt.penup()
    trt.goto(-250, -250)
    trt.left(90)
    trt.forward(height_value)
    trt.right(90)
    trt.pendown()
    height_value += 50
    for a in range(10):
        trt.speed(10.5)
        colormode(255)
        random_color = random.choice(rgb_colors)
        trt.color(random_color[0], random_color[1], random_color[2]) #r,g,b color tones
        trt.dot(20) #size of dot
        trt.penup()
        trt.forward(50)
        trt.pendown()

scr.exitonclick() #click for exit
