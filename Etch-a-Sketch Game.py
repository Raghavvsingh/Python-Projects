from turtle import Turtle,Screen

tim= Turtle()


def forward():
    tim.forward(20)
def backward():
    tim.back(20)
def right():
    tim.right(10)
def left():
    tim.left(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen=Screen()
screen.onkey(fun=forward,key="w")
screen.onkey(fun=backward,key="s")
screen.onkey(fun=right,key="d")
screen.onkey(fun=left,key="a")
screen.onkey(fun=clear,key="c")
screen.listen()
screen.exitonclick()
