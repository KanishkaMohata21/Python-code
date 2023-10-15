from turtle import Screen,Turtle
from pong_paddle import Paddle
from pong_ball import Ball
import time
from pong_scoreboard import Scoreboard

screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("PONG GAME")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
scoreboard=Scoreboard()

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.xcor()>600:
        ball.bounce_y()
    if ball.ycor()<-280 or ball.xcor()<-600:
        ball.bounce_y()
    if ball.distance(r_paddle)<50 and ball.xcor()>320:
        ball.bounce_x()
    if ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
    if ball.xcor()>380:
        scoreboard.l_point()
        ball.reset_position()
    if ball.xcor()<-380:
        scoreboard.r_point()
        ball.reset_position()




screen.exitonclick()