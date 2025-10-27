from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.y_move = 5
        self.x_move = 5
        self.bs = 0.02
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    def bounce(self):
        self.y_move *= -1
    def bounce_p(self):
        self.x_move *=-1
        self.bs *= 0.9
    def reset(self):
        self.goto(0,0)
        self.bounce_p()
        self.bs = 0.02