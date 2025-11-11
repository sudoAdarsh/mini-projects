from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard, Border, Speed
import time
my_screen = Screen()
my_screen.title("Pong")
my_screen.setup(height=600, width=800)
my_screen.bgcolor("white")
my_screen.tracer(0) 

left_paddle = Paddle((-380, 0))
right_paddle = Paddle((380, 0))
ball = Ball()
scoreboard = Scoreboard()
border = Border()
speed = Speed()

my_screen.listen()
my_screen.onkey(key="Up", fun= right_paddle.up)
my_screen.onkey(key="Down", fun= right_paddle.down)
my_screen.onkey(key="w", fun= left_paddle.up)
my_screen.onkey(key="s", fun= left_paddle.down)



game_is_on = True

while game_is_on:
    my_screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.xcor() < -355 and ball.xcor() > -380 and left_paddle.distance(ball) < 65) or (right_paddle.distance(ball) < 65 and ball.xcor() > 355 and ball.xcor() < 380):
        ball.bounce_x()
        speed.increase_speed()

    if ball.xcor() > 380: 
        ball.restart()
        scoreboard.r_point()
        speed.reset_speed()
    
    if ball.xcor() < -380:
        ball.restart()
        scoreboard.l_point()
        speed.reset_speed()

my_screen.exitonclick()