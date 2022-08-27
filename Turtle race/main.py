from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []

for turtle_index in range(0, 6):
    turtle_obj = Turtle(shape="turtle")
    turtle_obj.penup()
    turtle_obj.color(colors[turtle_index])
    turtle_obj.goto(x=-230, y=y_positions[turtle_index])
    turtles.append(turtle_obj)
if bet:
    is_race_on = True

while is_race_on:
    for obj in turtles:
        rand_distance = random.randint(0, 10)
        obj.forward(rand_distance)
        if obj.position()[0] >= 230:
            is_race_on = False
            if obj.pencolor() == bet:
                print(f"You won. The {obj.pencolor()} won.")

            else:
                print(f"You lost. The {obj.pencolor()} won.")

screen.exitonclick()