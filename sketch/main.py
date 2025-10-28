from turtle import Turtle, Screen

timmy = Turtle()
my_screen = Screen()

paces = 10

def move_ahead():
    timmy.forward(paces)

def turn_right():
    timmy.right(10)

def turn_left():
    timmy.left(10)

def move_back():
    timmy.backward(paces)


def clear_screen():
    timmy.reset()

my_screen.listen()
my_screen.onkey(key="w", fun=move_ahead)
my_screen.onkey(key="d", fun=turn_right)
my_screen.onkey(key="a", fun=turn_left)
my_screen.onkey(key="s", fun=move_back)
my_screen.onkey(key="c", fun=clear_screen)



my_screen.exitonclick()