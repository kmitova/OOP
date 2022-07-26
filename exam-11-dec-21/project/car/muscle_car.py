from project.car.car import Car


class MuscleCar(Car):
    def __init__(self, name, speed_limit):
        super().__init__(name, speed_limit)

    @property
    def max_speed_limit(self):
        return 450

    @property
    def min_speed_limit(self):
        return 250

