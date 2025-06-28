FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level=0
        self.penup()
        self.color("black")
        self.goto(-290,250)
        self.levels()

    def levels(self):
        self.clear()
        self.write(f"Level: {self.level}",align="left",font=FONT)

    def increase_level(self):
        self.level+=1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER." , align="center" , font=FONT)



