from turtle import Turtle
import os
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        self.level=1
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"LEVEL:{self.level}",align="Left",font=FONT)

    class ClearScreen:
        def clear(self):
            os.system("cls")

    def increase_level(self):
        self.level+=1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="Center",font=FONT)

        

