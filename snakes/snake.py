from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.main_snake = []
        self.create_snake()
        self.snake_head = self.main_snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("pink")
            new_segment.goto(position)              
            self.main_snake.append(new_segment)

    def extend(self):
        self.add_segment(self.main_snake[-1].position())

    def move(self):
        for segment in range(len(self.main_snake) - 1, 0, -1):
            new_x = self.main_snake[segment - 1].xcor()
            new_y = self.main_snake[segment - 1].ycor()
            self.main_snake[segment].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)