import turtle
import pandas


my_screen = turtle.Screen()
my_screen.title("Indian States Games")
my_screen.setup(width=800 ,height=953)
image = 'blank_map.gif'
my_screen.addshape(image)
turtle.shape(image)

tim = turtle.Turtle()
tim.hideturtle()
tim.penup()

""" get cordinates of states
def print_cords(x, y):
    print(f"{x}, {y}")
my_screen.listen()
my_screen.onscreenclick(print_cords)
"""
data = pandas.read_csv("state_cords.csv")

states_list = data["State"].to_list()

""" See all states on map 
for state in states_list:
    state_data = data[data.State == state]
    state_name = state_data.State.iloc[0]
    x_cor, y_cor = int(state_data.x.iloc[0]), int(state_data.y.iloc[0])
    tim.goto(x_cor, y_cor)
    tim.write(arg=state_name)
"""

correct_guess = []


while len(correct_guess) < 31:
    guess = my_screen.textinput(title=f"{len(correct_guess)}/31 States Guessed", prompt="Name a State").title()

    if guess == "Exit":
        missing_states = []
        for state in states_list:
            if state not in correct_guess:
                missing_states.append(state)
        new_data = pandas.DataFrame({"States" : missing_states})
        new_data.to_csv("States_to_learn.csv")
        break

    if guess in states_list:
        if guess not in correct_guess:
            correct_guess.append(guess)
            check_ans = data[data.State == guess]
            x_cor = int(check_ans.x.iloc[0])
            y_cor = int(check_ans.y.iloc[0])
            tim.goto(x_cor, y_cor)
            tim.write(arg=guess)

my_screen.clear()
tim.home()
evaluation = ""
score = len(correct_guess)
if score == 31:
    evaluation = 'You Guessed Them All Correctly'
elif score >= 20:
    evaluation = f"Good Work: {score}/31"
elif score >= 15:
    evaluation = f"Average Performance: {score}/31"
else:
    evaluation = f"Poor Performance: {score}/31"

tim.write(arg=f"{evaluation}", align="center", font=("Arial", 22, "bold"))

turtle.mainloop()