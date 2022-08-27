from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        with open(r"\Users\ireud\OneDrive\Desktop\data.txt", "a+") as file:
            content = file.readlines()
            if len(content) > 0:
                high_score = int(content[0])
                for i in range(1, len(content)):
                    if int(content[i]) > int(high_score):
                        high_score = int(content[i])

            else:
                high_score = 0

        self.high_score = high_score
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align= ALIGN, font= FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align= ALIGN, font= FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(r"\Users\ireud\OneDrive\Desktop\data.txt", "a+") as file:
                file.write(f"{self.high_score}\n")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #    self.goto(0, 0)
    #   self.write("GAME OVER", align=ALIGN, font=FONT)
    #    self.scores.append(self.score)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


