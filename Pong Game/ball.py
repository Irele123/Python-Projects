from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.width(20)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(0, 0)
        self.x_add = 10
        self.y_add = 10

    def move(self):
        x = self.xcor() + self.x_add
        y = self.ycor() + self.y_add
        self.goto(x, y)

    def bounce(self):
        self.y_add = -self.y_add

    def bounce_paddle(self):
        self.x_add = -self.x_add

    def restart(self):
        self.goto(0,0)



