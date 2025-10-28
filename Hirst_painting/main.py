# import colorgram
import turtle
import random

timmy = turtle.Turtle()
my_screen = turtle.Screen()
turtle.colormode(255)

# size_of_pallete = 30
# colors = colorgram.extract("image.jpg", size_of_pallete)
# pallete = []

# for color in range(size_of_pallete):
#     new_color = colors[color]
#     pallete.append((new_color.rgb.r, new_color.rgb.g, new_color.rgb.b))

color_list = [(204, 164, 107), (155, 73, 46), (52, 92, 123), (224, 201, 135), (171, 153, 40), (138, 31, 21), (132, 162, 185), (200, 91, 71), (48, 122, 87), (14, 99, 73), (95, 73, 75), (146, 178, 147), (72, 47, 38), (163, 142, 158), (234, 175, 165), (55, 46, 50), (184, 206, 172), (19, 85, 90), (144, 21, 24), (41, 62, 74), (82, 145, 128), (181, 87, 89), (41, 66, 90), (13, 71, 68), (213, 178, 183), (179, 191, 207)]


x = -350.0
y = -350.0


for column in range(15):
    for row in range(15):
        timmy.teleport(x, y)
        timmy.dot(20, random.choice(color_list))
        x += 50
    x = -350.0
    y += 50


print(timmy.pos())
my_screen.exitonclick()