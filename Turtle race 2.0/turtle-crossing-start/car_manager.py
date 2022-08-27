from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        choice = random.randint(1, 6)
        if choice == 1:
            color = random.choice(COLORS)
            car = Turtle("square")
            car.color(color)
            car.width(20)
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            x = 300
            y = random.randint(-250, 250)
            car.goto(x, y)
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)





