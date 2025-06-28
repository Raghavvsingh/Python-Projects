import turtle
from turtle import Turtle , Screen
import random
binod = Turtle()
binod.speed(0)
# colors = [
#     "mediumorchid",
#     "darkcyan",
#     "goldenrod",
#     "salmon",
#     "teal",
#     "tomato",
#     "slateblue",
#     "turquoise",
#     "firebrick",
#     "rosybrown"
# ]

turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r,g,b)

direction=[0,90,180,270]
binod.pensize(10)
for _ in range(300):
    binod.color(random_color())
    binod.forward(30)
    binod.setheading(random.choice(direction))


my_screen= Screen()
my_screen.exitonclick()