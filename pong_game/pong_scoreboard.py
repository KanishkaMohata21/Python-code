from turtle import Turtle
import os

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.l_score=0
        self.r_score=0
        self.hideturtle() 
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100,200)
        self.write(f"{self.l_score}",align="center",font=("Arial",24,"normal"))
        self.goto(100,200)
        self.write(f"{self.r_score}",align="center",font=("Arial",24,"normal"))
        self.hideturtle() 


        
    def l_point(self):
        clear_screen = ClearScreen()
        self.clear()
        self.l_score+=1
        self.update_scoreboard()

    def r_point(self):
        clear_screen = ClearScreen()
        self.clear()
        self.r_score+=1
        self.update_scoreboard()

class ClearScreen:
    def clear(self):
        os.system("cls")

                