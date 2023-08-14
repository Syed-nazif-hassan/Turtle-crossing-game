from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            random_y = random.randint(-250, 250)
            random_color = random.choice(COLORS)
            car = Turtle("square")
            car.color(random_color)
            car.penup()
            car.shapesize(1, 2)
            car.goto(300, random_y)
            self.all_cars.append(car)

    def car_move(self):
        for select_car in self.all_cars:
            select_car.backward(self.car_speed)

    def speed_increase(self):
        self.car_speed += MOVE_INCREMENT
