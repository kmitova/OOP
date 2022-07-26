from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    @staticmethod
    def car_factory(car_type, model, speed_limit):
        car_types = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}
        if car_type in car_types:
            car = car_types[car_type](model, speed_limit)
            return car

    def create_car(self, car_type, model, speed_limit):
        if any(c.model == model for c in self.cars):
            raise Exception(f"Car {model} is already created!")
        try:
            if car_type == 'MuscleCar':
                car = MuscleCar(model, speed_limit)
                self.cars.append(car)
                return f"{car_type} {model} is created."
            if car_type == 'SportsCar':
                car = SportsCar(model, speed_limit)
                self.cars.append(car)
                return f"{car_type} {model} is created."
        except RuntimeError:
            pass

    def create_driver(self, driver_name):
        if any(d.name == driver_name for d in self.drivers):
            raise Exception(f"Driver {driver_name} is already created!")
        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name):
        if any(r.name == race_name for r in self.races):
            raise Exception(f"Race {race_name} is already created!")
        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name, car_type):
        # 1: check if driver exists
        if not any(d.name == driver_name for d in self.drivers):
            raise Exception(f"Driver {driver_name} could not be found!")
#         2 check if there is an available car (not taken and exists)
        available_car = None
        # if car_type == "MuscleCar":
        for car in self.cars[::-1]:
            if car.__class__.__name__ == car_type and car.is_taken is False:
                available_car = car
                break
        if available_car is None:
            raise Exception(f"Car {car_type} could not be found!")
        # driver = None
        for d in self.drivers:
            if d.name == driver_name:
                driver = d
                if driver.car is not None:
                    old_car_model = driver.car.model
                    driver.car.is_taken = False
                    driver.car = None
                    driver.car = available_car
                    driver.car.is_taken = True
                    return f"Driver {driver_name} changed his car from {old_car_model} to {driver.car.model}."
                if driver.car is None:
                    driver.car = available_car
                    driver.car.is_taken = True
                    return f"Driver {driver_name} chose the car {driver.car.model}."

    def add_driver_to_race(self, race_name, driver_name):
        if not any(r.name == race_name for r in self.races):
            raise Exception(f"Race {race_name} could not be found!")
        if not any(d.name == driver_name for d in self.drivers):
            raise Exception(f"Driver {driver_name} could not be found!")
        driver = None
        # race = None
        for d in self.drivers:
            if d.name == driver_name:
                driver = d
        for r in self.races:
            if r.name == race_name:
                race = r
                if driver.car is None:
                    raise Exception(f"Driver {driver_name} could not participate in the race!")
                if driver.car is not None and driver not in race.drivers:
                    race.drivers.append(driver)
                    return f"Driver {driver_name} added in {race_name} race."
                return f"Driver {driver_name} is already added in {race_name} race."

    def start_race(self, race_name):
        if not any(r.name == race_name for r in self.races):
            raise Exception(f"Race {race_name} could not be found!")
        for r in self.races:
            if r.name == race_name:
                race = r
                if len(race.drivers) < 3:
                    raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
                winners = {}
                for driver in race.drivers:
                    winners[driver.name] = driver.car.speed_limit
                sorted_winners = sorted(winners.items(), key=lambda kvp: (-kvp[1], kvp[0]))[:3]
                result = ''
                for key, value in sorted_winners:
                    result += f"Driver {key} wins the {race_name} race with a speed of {value}.\n"
                    for d in race.drivers:
                        if d.name == key:
                            d.number_of_wins += 1
                return result.strip()

