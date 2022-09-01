import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()
screen.setup(width=600, height=600)


screen.listen()
screen.onkeypress(player.go_up, "Up")

cars = []

i = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 300:
        player.reset_position()
        scoreboard.next_level()
        scoreboard.refresh_scoreboard()
        car_manager.level_up()

screen.exitonclick()
