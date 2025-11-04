from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

my_screen = Screen()
my_screen.title("Pong")
my_screen.setup(height=600, width=800)
my_screen.bgcolor("black")
my_screen.tracer(0) 

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()

my_screen.listen()
my_screen.onkey(key="Up", fun= right_paddle.up)
my_screen.onkey(key="Down", fun= right_paddle.down)
my_screen.onkey(key="w", fun= left_paddle.up)
my_screen.onkey(key="s", fun= left_paddle.down)



game_is_on = True

while game_is_on:
    my_screen.update()
    time.sleep(0.05)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (left_paddle.distance(ball) < 50 and ball.xcor() > -320) or (right_paddle.distance(ball) < 50 and ball.xcor() > 320):
        ball.bounce_x()  

    if ball.xcor() > 380: 
        ball.restart()
    
    if ball.xcor() < -380:
        ball.restart()

my_screen.exitonclick()