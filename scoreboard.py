from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        """Creates a turtle that writes the scoreboard text."""
        super().__init__()
        self.score = 0
        self.ht() # Hides the turtle icon.
        self.color("white")
        self.teleport(y=260) # Teleports the text to the top of the screen.
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Generates a game over message."""
        self.teleport(0,0) # Teleports the text to the middle of the screen.
        self.color("red")
        self.write(arg=f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def update(self):
        """Updates the score board when the snake eats food."""
        self.score += 1 # Increases the score by 1 when the food is eaten.
        self.clear() # Clears the screen to prevent overlapping.
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)