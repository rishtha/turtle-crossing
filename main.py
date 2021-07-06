import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    #detect collision
    for car in car_manager.all_cars:
        if(car.distance(player)<25):
            game_is_on = False


    #successfull crossing
    if player.successful_crossing():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase()

scoreboard.game_over()
screen.exitonclick()
