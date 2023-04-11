from turtle import Turtle

class Pong(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=0.5, stretch_wid=5)
        self.penup()
        self.goto(position)
        self.color('white')

    def up(self):
        newY = self.ycor() + 20
        self.goto(self.xcor(),newY)
        

    def down(self):
        newY = self.ycor() - 20
        self.goto(self.xcor(),newY)





    




# screen.exitonclick()