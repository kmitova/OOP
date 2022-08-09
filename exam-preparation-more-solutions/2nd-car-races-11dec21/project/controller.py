from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        car = self.__find_existing_car_by_model(model)
        if car:
            raise Exception(f"Car {model} is already created!")
        new_car = self.__car_factory(car_type, speed_limit, model)
        if new_car:
            self.cars.append(new_car)
            return f"{car_type} {model} is created."

    def __car_factory(self, car_type, speed_limit, model):
        car = None
        if car_type == "MuscleCar":
            car = MuscleCar(model, speed_limit)
        if car_type == "SportsCar":
            car = SportsCar(model, speed_limit)
        return car

    def __find_existing_car_by_model(self, model):
        for car in self.cars:
            if car.model == model:
                return car

    def create_driver(self, driver_name: str):
        driver = self.__find_driver_by_name(driver_name)
        if driver:
            raise Exception(f"Driver {driver_name} is already created!")
        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def __find_driver_by_name(self, name):
        for d in self.drivers:
            if d.name == name:
                return d

    def __find_race_by_name(self, name):
        for r in self.races:
            if r.name == name:
                return r

    def create_race(self, race_name: str):
        race = self.__find_race_by_name(race_name)
        if race:
            raise Exception(f"Race {race_name} is already created!")
        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def __find_last_car_by_type(self, car_type):
        for i in range(len(self.cars)-1, -1, -1):
            car = self.cars[i]
            if not car.is_taken and car.__class__.__name__ == car_type:
                return car

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_driver_by_name(driver_name)
        car = self.__find_last_car_by_type(car_type)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        if not car:
            raise Exception(f"Car {car_type} could not be found!")
        if driver.car is not None:
            driver.car.is_taken = False
            old_model = driver.car.model
            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_model} to {car.model}."
        driver.car = car
        car.is_taken = True
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        driver = self.__find_driver_by_name(driver_name)
        race = self.__find_race_by_name(race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__find_race_by_name(race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        result = ''
        winners = sorted(self.drivers, key=lambda x: -x.car.speed_limit)[:3]
        for winner in winners:
            winner.number_of_wins += 1
            result += f"Driver {winner.name} wins the {race_name} race with a speed of {winner.car.speed_limit}.\n"
        return result.strip()


