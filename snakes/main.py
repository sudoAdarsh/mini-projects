from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time


my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("dark green")
my_screen.title("Snake game")
my_screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

my_screen.listen()

my_screen.onkey(key="Up", fun=snake.up)
my_screen.onkey(key="Down", fun=snake.down)
my_screen.onkey(key="Left", fun=snake.left)
my_screen.onkey(key="Right", fun=snake.right)

game_is_on = True

while game_is_on:
    my_screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score += 1
        score.refresh()

    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        game_is_on = False
        score.game_over()

    for segment in snake.main_snake[1 : ]:
        if snake.snake_head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

my_screen.exitonclick()