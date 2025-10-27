
from turtle import Screen, Turtle
from paddle import Paddle
s = Screen()
s.tracer(0)



rp = Paddle((500,0))
lp = Paddle((-500,0))




s.listen()
s.onkey(rp.up, 'Up')
s.onkey(lp.up, 'w')
s.onkey(rp.down, 'Down')
s.onkey(lp.down, 's')




game_on = True
while game_on:
    s.update()



s.exitonclick()



