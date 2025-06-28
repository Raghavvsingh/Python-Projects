from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

tim=Turtle()
my_screen = Screen()
my_screen.title("My Snake Game")
my_screen.bgcolor("black")
my_screen.setup(width=600,height=600)
my_screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

my_screen.listen()
my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.down,"Down")
my_screen.onkey(snake.right,"Right")
my_screen.onkey(snake.left,"Left")

game_is_on= True

while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

#Detect food collision and increase Score
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_l()
        scoreboard.increase_score()

#Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

#Detect collision with any part of the body
    for segment in snake.segments[1:]: #[1:] helps us to slice the segment list and take elements from 1 to end so we don't need to worry about head
        # if segment==snake.head:
        #     pass
        if snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()


my_screen.exitonclick()