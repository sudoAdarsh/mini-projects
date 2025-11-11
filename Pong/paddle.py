from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, cords):
        super().__init__()
        self.cords = cords
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        # self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.cords)

    def up(self):
        y_cord = self.ycor()
        self.goto(self.xcor(), y_cord + 30)

    def down(self):
        y_cord = self.ycor()
        self.goto(self.xcor(), y_cord - 30)
