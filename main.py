import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Score Update and Speed UP
    if player.ycor() > 240:
        score.update_score()
        player.reset_position()
        cars.level_up()

    # Detect Collision with car
    for car in cars.all_cars:
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False

    # Create and Move Cars
    cars.create_car()
    cars.move_cars()

screen.exitonclick()
