from turtle import Turtle
import random


class Food(Turtle):
    def __int__(self):
        super.__init__()

    def make_food(self):
        color_list = ["blue", "green", "red", "cyan", "magenta", "yellow", "white"]
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(color_list))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        color_list = ["blue", "green", "red", "cyan", "magenta", "yellow", "white"]
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.color(random.choice(color_list))
        self.goto(x=random_x, y=random_y)
