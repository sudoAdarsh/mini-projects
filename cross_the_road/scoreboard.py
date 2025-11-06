from turtle import Turtle
FONT = ("CourierPrime", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-230, 260)
        self.color("black")
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.level += 1 
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", align="center", font=FONT)
