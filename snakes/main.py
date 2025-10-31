from turtle import Turtle, Screen

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake game")

big_snake = []
starting_posistions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_posistions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(position)
    big_snake.append(new_segment) 

my_screen.exitonclick()