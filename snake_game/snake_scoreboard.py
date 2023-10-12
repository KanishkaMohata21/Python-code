from turtle import Turtle
import os

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open(r"C:\Users\ssc\Desktop\100.days.of.code\snake_game\data.txt") as data:
            self.highscore=int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.color("white")
        self.hideturtle() 
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score} High Score: {self.highscore}",align="center",font=("Arial",24,"normal"))
    
    def increase_score(self):
        self.score+=1
        clear_screen = ClearScreen()
        self.update_scoreboard()

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open(r"C:\Users\ssc\Desktop\100.days.of.code\snake_game\data.txt",mode="w") as data:
                data.write(f"{self.highscore}")

        self.score=0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER",align="center",font=("Arial",24,"normal"))

class ClearScreen:
    def clear(self):
        os.system("cls")

                