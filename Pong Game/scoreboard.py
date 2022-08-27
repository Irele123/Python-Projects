from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.write(f"{self.score}", align=ALIGN, font=FONT)
        self.hideturtle()

    def score_add(self):
        self.score = self.score + 1
        self.clear()
        self.goto(self.position)
        self.write(f"{self.score}", align=ALIGN, font=FONT)



