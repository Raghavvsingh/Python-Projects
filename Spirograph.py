import turtle
from turtle import Turtle , Screen
import random

binod = Turtle()
binod.speed(0)

# Generating a random color
turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r,g,b)

def spirograph(size_gap):
    for _ in range(int(360 / size_gap)):
        binod.color(random_color())
        binod.circle(200)#radius of circle
        current_heading = binod.heading()#Gives current direction
        binod.setheading(current_heading + size_gap)#Changes direction according to gap

spirograph(2) #Gap between circles

my_screen=Screen()
my_screen.exitonclick()