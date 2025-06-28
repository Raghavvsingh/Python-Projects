import random
import turtle
from turtle import Turtle,Screen

color=["purple","blue","green","yellow","orange","red"]
screen= Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make You Bet!",prompt="Which turtle will win? Enter the color: ")
race_is_on = False

y_coord=[-70,-40,-10,20,50,80]
all_turtles= []

def turtles():
    for index in range(0,6):
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.shape("turtle")
        new_turtle.color(color[index])
        new_turtle.goto(x=-230, y=y_coord[index])
        all_turtles.append(new_turtle)

turtles()

if user_bet:
    race_is_on=True

while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_is_on=False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} is the winner!")
            else:
                print(f"You've lost! The {winning_turtle} is the winner!")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()



