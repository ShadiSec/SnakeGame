from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        """Creates a turtle that writes the scoreboard text."""
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.ht() # Hides the turtle icon.
        self.color("white")
        self.teleport(y=260) # Teleports the text to the top of the screen.
        self.write(arg=f"Score: {self.score} | High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Generates a game over message."""
        self.teleport(0,0) # Teleports the text to the middle of the screen.
        self.color("red")
        self.write(arg=f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.update()

    def get_high_score(self):
        """Get the high score from the data file."""
        with open("data.txt") as file:
            content = file.read()
            return int(content)

    def save_high_score(self):
        """Save the high score to the data file."""
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))

    def update(self):
        """Updates the score board when the snake eats food."""
        self.clear() # Clears the screen to prevent overlapping.
        self.write(arg=f"Score: {self.score} | High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1  # Increases the score by 1 when the food is eaten.