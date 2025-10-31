from turtle import Turtle, Screen
from random import randint


my_screen = Screen()
my_screen.setup(height=500, width=750)

user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ") 

all_turtles = []

colors= ["red", "orange","yellow", "green", "blue", "indigo"]
y_cord = [-100, -50, 0, 50, 100, 150]


for _ in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[_])
    new_turtle.goto(-350, y_cord[_])
    all_turtles.append(new_turtle)

if user_bet:
    race = True

while race:
    for turtle in all_turtles:
        
        if turtle.xcor() > 343:
            race = False
            winning_color = turtle.pencolor()

            if user_bet == winning_color:
                print(f"You've won! the {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! the {winning_color} turtle is the winner!")
        
        random_distance = randint(1, 10)
        turtle.forward(random_distance)





my_screen.exitonclick()