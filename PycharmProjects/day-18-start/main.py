import turtle as turtle_module
import random

turtle_module.colormode(255)
tom = turtle_module.Turtle()
position = 0
tom.up()
tom.hideturtle()
color_list = [(26, 36, 45), (111, 93, 83), (173, 156, 141), (49, 35, 42), (248, 244, 246), (74, 92, 104),
              (245, 250, 248), (87, 98, 94), (46, 38, 35), (239, 240, 243), (103, 73, 78), (147, 159, 152),
              (135, 155, 165),
              (36, 49, 46), (132, 36, 43), (124, 37, 31), (176, 155, 159), (187, 98, 85), (138, 131, 110),
              (206, 196, 166),
              (221, 55, 68), (57, 61, 75), (49, 69, 74), (223, 177, 167), (53, 69, 66), (119, 133, 126), (97, 137, 153),
              (73, 68, 47), (217, 177, 184)]

tom.setheading(225)
tom.forward(300)
tom.setheading(0)


def printing():
    for _ in range(10):
        for _ in range(10):
            tom.dot(20, random.choice(color_list))
            tom.forward(50)

        for _ in range(1):
            tom.setheading(90)
            tom.forward(50)
            tom.setheading(180)
            tom.forward(500)
            tom.setheading(0)


printing()

screen = turtle_module.Screen()
screen.exitonclick()
