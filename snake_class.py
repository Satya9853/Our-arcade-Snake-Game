import turtle as t
import Score_board_class as s
POSITION = [(-20, 0), (-40, 0), (-60, 0)]
class Snake:
    def __init__(self):
        self.snake_bodies = []
        self.create_snake()
        self.heading = self.snake_bodies[0]


    def create_snake(self):
        for i in POSITION:
            self.snake_body(i)

    def tail_move(self):
        self.snake_body(self.snake_bodies[-1].position())

    def reset_snake(self):
        for seg in self.snake_bodies:
            seg.goto(1000, 1000)
        self.snake_bodies.clear()
        self.create_snake()
        self.heading = self.snake_bodies[0]

    def snake_body(self, position):
        snake = t.Turtle('circle')
        snake.penup()
        snake.color('white')
        snake.goto(position)
        self.snake_bodies.append(snake)

    def move(self):
        for i in range(len(self.snake_bodies)-1, 0, -1):
            new_x = self.snake_bodies[i - 1].xcor()
            new_y = self.snake_bodies[i - 1].ycor()
            self.snake_bodies[i].goto(new_x, new_y)
        self.heading.forward(20)



    def left_side(self):
        if self.heading.heading() != 0:
            self.heading.setheading(180)

    def right_side(self):
        if self.heading.heading() != 180:
            self.heading.setheading(0)

    def upper_side(self):
        if self.heading.heading() != 270:
            self.heading.setheading(90)

    def down_side(self):
        if self.heading.heading() != 90:
            self.heading.setheading(270)
