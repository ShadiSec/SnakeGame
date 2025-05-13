from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        """Creates a circular food object on screen."""
        super().__init__() # Inherit the attributes and methods of the Turtle class.
        self.shape("circle") # Makes the new object circular.
        self.shapesize(stretch_wid=0.5, stretch_len=0.5) # Shrinks the object from 20x20 to 10x10.
        self.color("orange") # Sets the color of the object
        self.refresh() # Creates a food object at a random location.

    def refresh(self):
        """Moves the food object to a random location."""
        random_x = random.randint(-260, 260)  # Generates a random x-axis.
        random_y = random.randint(-260, 260)  # Generates a random y-axis.
        self.teleport(random_x, random_y)  # Teleports the newly created object to the random coordinates.