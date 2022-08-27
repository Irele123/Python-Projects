import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
speed = 0.1

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")
game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    car.create_cars()
    car.move()

    for cars in car.all_cars:
        if cars.distance(player) < 20:
            # time.sleep(5)
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() >= player.end:
        player.reset()
        scoreboard.add()
        speed = speed - 0.01

screen.exitonclick()