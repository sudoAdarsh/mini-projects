import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

timmy = Player()
score = Scoreboard()
car_manager = CarManager()


screen.listen()

screen.onkey(fun=timmy.move, key="Up")

game_is_on = True
while game_is_on:

    # start spawing car
    car_manager.spawn_cars()
    car_manager.move_cars()
    # check timmy reached next level
    if timmy.ycor() > 280:
        timmy.next_level()
        score.update_scoreboard()
        car_manager.increase_speed()
    
    for _ in range(len(car_manager.all_cars)):
        if timmy.distance(car_manager.all_cars[_]) < 30:
            game_is_on = False
            score.game_over()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()