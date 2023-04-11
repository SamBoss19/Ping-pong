from turtle import Turtle

FONT = ("Cambria",20,"normal")
class ScoreR (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(225,315)
        self.hideturtle()
        # self.shape("none")
        self.write(f"Score: {self.score}", move = False, align = "left", font = FONT )
    def increaseR(self):
        self.clear()
        self.score += 1  
        print(self.score)
        self.write(f"Score: {self.score}", move = False, align = "left", font = FONT)
    def gameover(self):
        self.goto(-70,0)
        self.write(f"Gameover.", move = False, align = "left", font = ("Cambria",20,"normal"))




class ScoreL (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(-225,315)
        self.hideturtle()
        # self.shape("none")
        self.write(f"Score: {self.score}", move = False, align = "right", font = FONT )
    def increaseL(self):
        self.clear()
        self.score += 1  
        print(self.score)
        self.write(f"Score: {self.score}", move = False, align = "right", font = FONT)
    def gameover(self):
        self.goto(0,0)
        self.write(f"Gameover.", move = False, align = "right", font = ("Cambria",20,"normal"))