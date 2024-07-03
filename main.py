# ========================================================================== #
# Programmer : Walter Reeves
#
# Description:
#   This program plays a traditional snake game.
#
# Enhancement:
#   Add triangle shaped segments.
#   Add a way for the triangle segments to change direction.
# ========================================================================== #
from food import Food
from score import Score
from snake import Snake
from turtle import Screen

import time

# Global Variables
food = Food()
game_is_on = True
score = Score()
snake = Snake()

# Initialize the screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Get keystrokes from user.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    # Sets the screen latency.
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Moves the food when eaten.
    if snake.head.distance(food) < 15:
        food.relocate()
        snake.extend()
        score.increase_score()

    # Ends the game when the snake goes out-of-bounds.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or \
            snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.reset()

    # Checks to see if the snake is touching itself.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.reset()
            snake.reset()


screen.exitonclick()
