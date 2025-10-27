import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreb
s = Screen()
s.tracer(0)

b = Ball()

rp = Paddle((700,0))
lp = Paddle((-700,0))
sc = Scoreb()

b.move()
sc.updates()
s.listen()
s.onkey(rp.up, 'Up')
s.onkey(lp.up, 'w')
s.onkey(rp.down, 'Down')
s.onkey(lp.down, 's')




game_on = True
while game_on:
    time.sleep(b.bs)
    s.update()
    b.move()
    if b.ycor() > 400 or b.ycor() <-400 :
        b.bounce()

    if b.distance(rp)<50  and b.xcor() > 700-40 or b.distance(lp) < 50 and b.xcor() < -700+40:

        b.bounce_p()
    if b.xcor() > 700:
        b.reset()
        sc.l_point()

    if b.xcor() <-700:
        b.reset()
        sc.r_point()

s.exitonclick()



