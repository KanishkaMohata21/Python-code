from turtle import Turtle,Screen
import random

is_race_on=False
screen=Screen()
all_turtles=[]
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race?,Enter a colour:")
colors=["red","orange","yellow","green","blue","purple"]
y_positions=[-70,-40,-10,20,50,80]

for t in range(0,6):
    turtles=Turtle(shape="turtle")
    turtles.penup()
    turtles.goto(x=-230,y=y_positions[t])
    turtles.color(colors[t])
    all_turtles.append(turtles)

if user_bet:
    is_race_on=True

while is_race_on:
    for t in all_turtles:
        if t.xcor()>230:
            winning_color=t.pencolor()
            is_race_on=False
            if winning_color==user_bet:
                print("YOU WON THE BET")    
            else:
                print(f"YOU LOST THE BET,WINING TURTLE IS {winning_color}")    
        ran_distance=random.randint(0,10)
        t.forward(ran_distance)




screen.exitonclick()
