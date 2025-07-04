import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

score = 0
answer_storing = []

while len(answer_storing) < 50:
    answer = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")
    answer = answer.title()

    if answer== "Exit" :
        break
    if answer in states and answer not in answer_storing:
        score += 1
        answer_storing.append(answer)

        state_data = data[data["state"] == answer]
        x = state_data["x"].iloc[0]
        y = state_data["y"].iloc[0]

        marker = turtle.Turtle()
        marker.hideturtle()
        marker.penup()
        marker.goto(x, y)
        marker.write(answer, align="center", font=("Courier", 12, "normal"))

remaining=[]

for state in states:
    if state not in answer_storing:
        remaining.append(state)

remaing_states_csv =pandas.DataFrame(remaining)
remaing_states_csv.to_csv("Remaining States.csv")

