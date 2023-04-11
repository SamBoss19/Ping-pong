from pong import Pong
from ball import Ball
from turtle import Turtle, Screen
import time
import random
from scoreboard import ScoreR, ScoreL
screen =Screen()
screen.setup(width = 900, height= 700)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong Game")
Left_Score = ScoreL()
Right_score = ScoreR()

r_paddle = Pong((440,0))
l_paddle =Pong((-440,0))
ball = Ball()
gaming = True
screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")
while gaming: 
    screen.update()
    time.sleep(0.05)
    ball.move()
    if ball.ycor() > 340 or ball.ycor() < -340:
        ball.bounce_top()
    if ball.distance(r_paddle) < 50 and ball.xcor() >425:
        ball.bounce_paddle()
        Right_score.increaseR()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -425:
        ball.bounce_paddle()
        Left_Score.increaseL()
    elif ball.xcor() > 445 or ball.xcor() < -445:
        Right_score.gameover()
        gaming = False

    


        



    
    


screen.exitonclick()