from project.car.car import Car


class SportsCar(Car):
    MAX_SPEED_LIMIT = 600
    MIN_SPEED_LIMIT = 400

    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

