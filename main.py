import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
tim.pensize(15)
tim.speed("fastest")

"""colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]"""
# Using list
directions = [0, 90, 180, 270]

# Using turple
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for _ in range(200):
    # tim.color(random.choice(colours))
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
s = Screen()
screen = Screen()
s.exitonclick()
