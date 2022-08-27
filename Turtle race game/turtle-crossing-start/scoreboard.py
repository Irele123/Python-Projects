from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        position = (-300, 250)
        self.color("black")
        self.penup()
        self.goto(position)
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)
        self.hideturtle()

    def add(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)


