from snake_class import Snake
from turtle import Screen
import time
display = Screen()
display.listen()
display.setup(600, 600)
display.bgcolor('black')
display.title('Welcome to Snake World')
snake = Snake()
display.tracer(0)

def left_side():
    snake.snake_bodies[0].left(90)


def right_side():
    snake.snake_bodies[0].right(90)


display.onkeypress(fun=left_side, key='a')
display.onkeypress(fun=right_side, key='d')
while True:
    display.update()
    time.sleep(0.1)
    snake.move()

display.exitonclick()
