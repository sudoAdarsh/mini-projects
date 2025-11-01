from turtle import Turtle

ALIGNMENT = "center"
FONT = ("JetBrains Mono", 16, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.teleport(x=0 ,y=270)
        self.hideturtle()
        self.refresh()


    def refresh(self):
        self.clear()
        self.write(f"Score : {self.score}", align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.teleport(0, 0)
        self.write(f"GAME OVER", align = ALIGNMENT, font = FONT)