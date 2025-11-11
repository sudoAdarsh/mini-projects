from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        # self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 265)
        self.write(arg=f"Player A: {self.r_score}", align="center", font=("JetBrains Mono", 20, "normal"))
        self.goto(100, 265)
        self.write(arg=f"Player B: {self.l_score}", align="center", font=("JetBrains Mono", 20, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        y_pos = 300
        self.goto(0, y_pos)
        self.setheading(270)

        for lines in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)


class Speed(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("blue")
        self.goto(-390, 270)
        self.speed = 1
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Speed: {self.speed}", font=("JetBrains Mono", 13, "normal"))
    
    def increase_speed(self):
        self.speed += 1
        self.update()

    def reset_speed(self):
        self.speed = 1
        self.update()