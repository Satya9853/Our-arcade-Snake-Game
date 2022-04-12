import turtle as t
import random
import time

# defining object from class

display = t.Screen()
snake_bodies = []
display.setup(600, 600)
display.bgcolor('black')
display.title('Welcome to Snake World')
display.listen()

# defining function for user keyword


is_game_on = True
# basically display.tracer(0) turns off the detection of turtle movement or operation of the turtle in the screen
# until it is manually updated
display.tracer(0)
x = 0
for i in range(3):
    snake = t.Turtle('square')
    snake.penup()
    snake.color('white')
    snake.setposition(x, 0)
    snake_bodies.append(snake)
    x -= 10


def left_side():
    snake_bodies[0].left(90)


def right_side():
    snake_bodies[0].right(90)


display.onkeypress(fun=left_side, key='a')
display.onkeypress(fun=right_side, key='d')
while is_game_on:
                                                    # time sleep delays the program or set the time at which the code
                                                    # will execute after the mention time
                                                    # this is what i was telling about in the tracer this help us to
                                                    # manually update the tracer after thi line the
                                                     # operation of our turtle will be conducted
    time.sleep(0.1)
    display.update()
    for i in range(2, 0, -1):
        new_x = snake_bodies[i - 1].xcor()
        new_y = snake_bodies[i - 1].ycor()
        snake_bodies[i].goto(new_x, new_y)
    snake_bodies[0].forward(20)

display.exitonclick()
