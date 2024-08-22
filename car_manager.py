from turtle import Turtle
import random
LANE=[]
for i in range(-14,13):
    LANE.append(20*i)
print(LANE)
X_START=[]
for i in range(30,600):
    X_START.append(10*i)

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10
DIR = 180


class Car:
    def __init__(self):
        self.car = []
        self.create_car()

    def create_car(self):

        color = random.choice(COLORS)
        for i in range(0, 3):
            car = Turtle(shape='square')
            car.penup()
            car.color(color)
            car.setheading(DIR)
            self.car.append(car)
        self.car_home(y=random.choice(LANE))

    def move_one_car(self):
        if self.car[2].xcor() == -300:
            self.car_home(y=random.choice(LANE))
        for seg in self.car:
            seg.forward(STARTING_MOVE_DISTANCE)

    def car_home(self, y):
        self.car[0].resizemode("user")
        x = random.choice(X_START)
        self.car[0].shapesize(0.5, 0.5, 0)
        self.car[0].goto(-15 + x - 5, y)
        self.car[1].goto(x - 5, y)
        self.car[2].resizemode("user")
        self.car[2].shapesize(0.5, 0.5, 0)
        self.car[2].goto(15 + x - 5, y)



class CarManager:
    def __init__(self):
        self.car_list=[]
        for i in range(0, 300):
            new_car = Car()
            self.car_list.append(new_car)
    #
    # def avoid_crash(self):
    #     for k in self.car_list:
    #         for j in self.car_list:
    #             if k.car[0].distance(j.car[0]):
    #                 pass
    #             else:




