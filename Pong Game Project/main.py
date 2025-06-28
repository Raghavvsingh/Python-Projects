from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

my_screen=Screen()
my_screen.setup(width=800,height=600)
my_screen.bgcolor("black")
my_screen.title("LETS PLAY PONG")
my_screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
score=Scoreboard()

my_screen.listen()
my_screen.onkey(r_paddle.move_up,"Up")
my_screen.onkey(r_paddle.move_down,"Down")
my_screen.onkey(l_paddle.move_up,"w")
my_screen.onkey(l_paddle.move_down,"s")



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    my_screen.update()
    ball.move()

# Ball bouncing from top and bottom wall
    if ball.ycor()>280 or ball.ycor() < -280:
        ball.bounce_y()

# Ball bouncing if paddle hit
    if ball.distance(r_paddle)<50 and ball.xcor() > 320 or ball.distance(l_paddle)<50 and ball.xcor() < -320:
        ball.bounce_x()

# Ball miss from right paddle
    if ball.xcor()>380 :
        ball.reset()
        score.l_scores()

# Ball miss from left paddle
    if ball.xcor()<-380:
        ball.reset()
        score.r_scores()







my_screen.exitonclick()