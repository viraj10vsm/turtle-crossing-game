import time,random
from turtle import Screen
from player import Player
from car_manager import Car, CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600) 
screen.bgcolor('grey')
screen.tracer(0)
turtle = Player()

car_manager = CarManager()
screen.listen()
screen.onkey(key="Up", fun=turtle.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in car_manager.car_list:
        for j in car_manager.car_list:
            if car == j :
                continue
            if car.car[0].distance(j.car[0]) < 30:
                j.car_home(y=random.randint(330, 700))

        car.move_one_car()
        # game_is_on = False

screen.exitonclick()