# import colorgram
#
# colors = colorgram.extract('image.jpg', 50)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
import turtle
from turtle import Turtle, Screen


turtle.colormode(255)
tom = Turtle()
screen = Screen()
tom.speed(0)
tom.penup()
tom.hideturtle()

canvas = tom.getscreen().getcanvas()

tom.setheading(225)
tom.forward(300)
tom.setheading(0)


colors = [(244, 228, 79), (162, 75, 42), (216, 146, 90), (23, 30, 61), (124, 160, 218), (54, 89, 145), (45, 36, 30),
          (40, 48, 114), (29, 44, 34), (147, 56, 81), (131, 31, 43), (203, 82, 120), (146, 31, 25), (214, 80, 55),
          (69, 31, 41), (67, 113, 77), (133, 182, 164), (94, 105, 200), (193, 140, 155), (72, 79, 40), (96, 162, 82),
          (153, 207, 220), (156, 186, 235), (48, 87, 32), (171, 165, 69), (229, 169, 185), (144, 211, 191),
          (233, 172, 161), (244, 220, 4), (88, 140, 156), (41, 76, 85)]

for count in range(1, 101):
    tom.dot(20, random.choice(colors))
    tom.forward(50)

    if count % 10 == 0:
        tom.left(90)
        tom.forward(50)
        tom.left(90)
        tom.forward(500)
        tom.setheading(0)


canvas.postscript(file="turtle_img.ps")
screen.exitonclick()
