from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

screen = Screen() # Creates a screen.
screen.setup(width=600, height=600) # Sets the screen dimensions.
screen.tracer(0) # Turns off the turtle moving animation.
screen.bgcolor("black") # Sets the screen background to black.
screen.title("Susie The Snake") # Sets the window title.

snake = Snake() # Creates a snake.
food = Food() # Creates a food object.
scoreboard = Scoreboard() # Creates the score text.

# Listen for user keystrokes.
screen.listen()
screen.onkey(fun=snake.up, key="w") # Calls the up Method of the Snake class when the "w" key is pressed.
screen.onkey(fun=snake.down, key="s") # Calls the down Method of the Snake class when the "s" key is pressed.
screen.onkey(fun=snake.left, key="a") # Calls the left Method of the Snake class when the "a" key is pressed.
screen.onkey(fun=snake.right, key="d") # Calls the right Method of the Snake class when the "d" key is pressed.

is_on = True

# Keeps the snake moving until the game is over.
while is_on:
    screen.update() # Updates the screen everytime the snake moves. (This makes all squares in the body appear to be moving at once.)
    time.sleep(.1) # Slows down the speed at which the screen updates.
    snake.move() # Moves the snake forward.

    # Detects collision between the snake and the food.
    if snake.head.distance(food) < 15: # Checks if the snake head is within 15pts of the food.
        food.refresh() # Teleports the food to a random location.
        scoreboard.update() # Updates the scoreboard everytime food is eaten.
        snake.extend() # Extend the snake everytime food is eaten.

    # Detects the collision with the wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_on = False # Stops the snake from moving.
        scoreboard.game_over() # Displays a game over message on screen.

    # Detects the collision with the tail.
    for square in snake.all_squares[1:]: # Loops through all squares in the snake body except for the snake head.
        if snake.head.distance(square) < 15: # Checks if the head is within 15pts of the body squares.
            is_on = False # Stops the snake from moving.
            scoreboard.game_over() # Displays a game over message.

screen.exitonclick()