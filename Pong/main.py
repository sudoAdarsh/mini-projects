from turtle import Screen
from paddle import Paddle

my_screen = Screen()
my_screen.title("Pong")
my_screen.setup(height=600, width=800)
my_screen.bgcolor("black")

paddle_position = [(350, 0), (-350, 0)]

paddles = []

for paddle in paddle_position:
    new_paddle = Paddle()
    new_paddle.goto(paddle)
    new_paddle.create_paddle()
    paddles.append(new_paddle)

left_paddle = paddles[1]
right_paddle = paddles[0]

my_screen.listen()

my_screen.onkey(key="Up", fun= right_paddle.up)
my_screen.onkey(key="Down", fun= right_paddle.down)


my_screen.onkey(key="w", fun= left_paddle.up)
my_screen.onkey(key="s", fun= left_paddle.down)


my_screen.exitonclick()