from turtle import Turtle
class Scoreb(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
    def updates(self):
        self.clear()
        self.goto(-100,300)
        self.write(self.l_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 300)
        self.write(self.r_score, align='center', font=('Courier', 80, 'normal'))
    def l_point(self):
        self.l_score += 1
        self.updates()
    def r_point(self):
        self.r_score += 1
        self.updates()

