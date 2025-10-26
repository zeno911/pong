
from turtle import Screen, Turtle
from paddle import Paddle
s = Screen()
s.tracer(0)
paddle = Turtle()



game_on = True
while game_on:
    s.update()


rp = Paddle((500,0))
lp = Paddle((-500,0))

s.update()


s.exitonclick()



