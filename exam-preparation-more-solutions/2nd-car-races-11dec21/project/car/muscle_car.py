from project.car.car import Car


class MuscleCar(Car):
    MAX_SPEED_LIMIT = 450
    MIN_SPEED_LIMIT = 250

    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

