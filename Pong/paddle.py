from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=10, stretch_len=2)
        self.penup()

    def up(self):
        x_cord = self.xcor()
        y_cord = self.ycor()
        self.goto(x_cord, y_cord + 20)

    def down(self):
        x_cord = self.xcor()
        y_cord = self.ycor()
        self.goto(x_cord, y_cord - 20)
