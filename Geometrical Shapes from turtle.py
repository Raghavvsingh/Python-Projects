import turtle
from turtle import Turtle , Screen

binod=Turtle()
binod.speed(0)
def triangle(binod):
    for _ in range(3):
        binod.forward(100)
        binod.right(120)

def square(binod):
    for _ in range(4):
        binod.forward(100)
        binod.right(90)


def shapes(binod):
    n = 5
    for angle in [72,60,51,45,40,36]:
        for _ in range(n):
            binod.forward(100)
            binod.right(angle)
        n+=1
        if n==11:
            break

binod.color("green")
triangle(binod)
square(binod)
shapes(binod)

my_screen= Screen()
my_screen.exitonclick()