import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
screen.listen()
screen.onkey(player.move,"Up")

cars=CarManager()

scoreboard=Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_car()

#Detect Collision With cars
    for car in cars.all_cars:
        if car.distance(player)<20:
            scoreboard.game_over()
            game_is_on=False

#Check if turtle is at top boundary
    if player.increase_level():
        player.go_to_start()
        cars.increase_speed()
        scoreboard.increase_level()
        scoreboard.levels()

screen.exitonclick()
