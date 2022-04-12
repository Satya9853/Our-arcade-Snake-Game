from snake_class import Snake
from turtle import Screen
from food_for_snake import Food
from Score_board_class import ScoreBoard
import time
SNAKE_SPEED = 0.1
display = Screen()
display.setup(width=600, height=600)
display.listen()
display.bgcolor('black')
display.title('Welcome to Snake World created by satya bhusan prusty')

# Defining classes
snake = Snake()
food = Food()
name_turtle = ScoreBoard()
display.tracer(0)


display.onkeypress(fun=snake.left_side, key='Left')
display.onkeypress(fun=snake.right_side, key='Right')
display.onkeypress(fun=snake.upper_side, key='Up')
display.onkeypress(fun=snake.down_side, key='Down')
is_game_on = True
while is_game_on:
    display.update()
    time.sleep(SNAKE_SPEED)
    snake.move()
    name_turtle.update_scoreboard()
    # detect food
    if snake.heading.distance(food) < 15:
        name_turtle.scoring_increment()
        food.refresh()
        snake.tail_move()

    # detect wall collision
    if snake.heading.xcor() > 280 or snake.heading.xcor() < -300 or snake.heading.ycor() > 300 or snake.heading.ycor() < -280:
        name_turtle.highscore_track()
        snake.reset_snake()
        name_turtle.game_over()
        is_game_on = False
    # detect body collision
    for segment in snake.snake_bodies[1:]:
        if snake.heading.distance(segment) < 1:
            name_turtle.highscore_track()
            snake.reset_snake()
            name_turtle.game_over()
            is_game_on = False

display.exitonclick()
