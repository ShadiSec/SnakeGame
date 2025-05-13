from turtle import Turtle

SQUARE_POSITIONS = [(0,0), (-20,0), (-40,0)] # Sets the starting position for all squares of the snake body. (Adding to this will increase the
# original size of the snake.)

MOVE_DISTANCE = 20 # Sets the distance the snake moves with each step.

# Sets the directions the turtle will face.
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        """Creates a snake."""
        self.all_squares = [] # Will propagate with the newly created squares.
        self.create_snake() # Creates the snake body.
        self.head = self.all_squares[0] # Sets the head of the snake to "head".

    def create_snake(self):
        """
        Creates a square for each coordinate in the square_positions list.
        This creates the original snake body.
        """
        for position in SQUARE_POSITIONS:
            self.add_square(position)

    def add_square(self, position):
        """Adds a square to the snake based on the position given."""
        new_turtle = Turtle("square")  # Sets the turtle shape to square.
        new_turtle.color("white")  # Sets the square color to white.
        new_turtle.penup()  # Removes the drawing animation while moving.
        new_turtle.goto(position)  # Sends the square to its proper starting position.
        self.all_squares.append(new_turtle)  # Adds the newly created square to the all_squares list for ability to control later on.

    def extend(self):
        """Adds a square to the end of the snake based on the coordinates of the last square in the body."""
        self.add_square(self.all_squares[-1].position())

    # Creates a method to move the snake in an orderly fashion.
    def move(self):
        """
        Moves each square in the snake body except the head to the position of the square in front of it.
        """
        # Locates each square starting from the last square.
        for current_square in range(len(self.all_squares) - 1, 0, -1):
            new_x = self.all_squares[current_square - 1].xcor() # Creates a new x position from the x-coordinate of the square in front.
            new_y = self.all_squares[current_square - 1].ycor() # Creates a new y position from the y-coordinate of the square in front.
            self.all_squares[current_square].goto(new_x, new_y) # Moves the current square to the position of the square in front of it.
        self.all_squares[0].forward(MOVE_DISTANCE) # Moves the head of the snake by 20pts.

    def up(self):
        """Turns the head of the snake North."""
        # Stops the snake from moving down if it's currently moving up.
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Turns the head of the snake South"""
        # Stops the snake from moving up if it's currently moving down.
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Turns the head of the snake West."""
        # Stops the snake from moving right if it's currently moving left.
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Turns the head of the snake East."""
        # Stops the snake from moving left if it's currently moving right.
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)