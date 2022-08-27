import turtle
import pandas

ALIGN = "center"
FONT = ("Courier", 8, "normal")

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
missing_states = []

for states in all_states:
    missing_states.append(states)

guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/States Correct", prompt="What's another states name")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        print(missing_states)
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        obj = turtle.Turtle()
        obj.hideturtle()
        obj.penup()
        correct_state = data[data.state == answer_state]
        obj.goto(int(correct_state.x), int(correct_state.y))
        obj.write(answer_state, align=ALIGN, font=FONT)
        missing_states.remove(answer_state)

remain_states = pandas.DataFrame(all_states)
remain_states.to_csv("states_to_learn.csv")

screen.exitonclick()
