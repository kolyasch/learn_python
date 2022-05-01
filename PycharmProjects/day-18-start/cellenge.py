from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape('triangle')
tim.color('black', 'blue')


colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape():

    for _ in range(360):
        tim.circle(100)
        tim.color(random.choice(colors))
draw_shape()
screen = Screen()
screen.exitonclick()