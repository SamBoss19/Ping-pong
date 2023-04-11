from turtle import Turtle
import random
no = [1,2]
for hot in no:
    turn = random.randint(0,2)
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.goto(0,0)
        self.xmove = 5
        self.ymove = 5

    def move(self):
        newx = self.xcor() + self.xmove
        newy = self.ycor() + self.ymove
        self.goto(newx,newy)

    def bounce_top(self):
        self.ymove *= -1
    
    def bounce_paddle(self):
        self.xmove *= -1

    def gameover(self):
        self.goto(0,0)
        



    

        

   