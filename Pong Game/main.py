from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

sleep_time = 0.1
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "x")

l_scoreboard = Scoreboard((-100, 200))
r_scoreboard = Scoreboard((100, 200))

game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    ball.move()

    touch = False
    # Detect collision with wall
    if ball.xcor() > 380 or ball.ycor() > 280 or ball.xcor() < -380 or ball.ycor() < -280:
        ball.bounce()

    # Detect collision with right paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_paddle()
        # sleep_time = sleep_time - 0.01
        touch = True

    if not touch and ball.xcor() > 380:
        ball.restart()
        sleep_time = 0.1
        l_scoreboard.score_add()

    if not touch and ball.xcor() < -380:
        ball.restart()
        sleep_time = 0.1
        r_scoreboard.score_add()

screen.exitonclick()

