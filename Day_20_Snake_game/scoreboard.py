from turtle import Turtle
## CONSTANTS
ALIGNMENT = "center"
FONT =("Courier", 24, "normal")

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score = 0
    self.color("White")
    self.penup()
    self.goto(0, 270)
    self.update_scoreboard()
    self.hideturtle()

  def update_scoreboard(self):
    self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

  def game_over(self):
    self.goto(0, 0)
    self.write("GAME OVER", align=ALIGNMENT, font=FONT)
  

  def increase_score(self):
    self.score += 1
    self.clear()
    self.update_scoreboard()