from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful = 0
        self.unsuccessful = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut:
            return f"{name} is already added."
        if astronaut_type not in ["Biologist", "Geodesist", "Meteorologist"]:
            raise Exception("Astronaut type is not valid!")

        new_astronaut = self.__create_new_astronaut(astronaut_type, name)
        self.astronaut_repository.add(new_astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def __create_new_astronaut(self, astronaut_type, name):
        astronaut = None
        if astronaut_type == 'Biologist':
            astronaut = Biologist(name)
        if astronaut_type == 'Geodesist':
            astronaut = Geodesist(name)
        if astronaut_type == 'Meteorologist':
            astronaut = Meteorologist(name)
        return astronaut

    def add_planet(self, name: str, items: str):
        planet = self.planet_repository.find_by_name(name)
        if planet:
            return f"{name} is already added."
        items_list = items.split(', ')
        new_planet = Planet(name)
        new_planet.items = items_list
        self.planet_repository.add(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")
        astronauts = self.find_astronauts_for_mission()
        # if len(astronauts) > 5:
        #     astronauts = astronauts[:5]
        if len(astronauts) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")
        explorers = 0

        # tricky for loop, version commented version below gives 141/150
        for astronaut in astronauts:
            if len(planet.items) == 0:
                break
            while astronaut.oxygen > 0 and len(planet.items) > 0:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
            explorers += 1
        # for astronaut in astronauts:
        #     if len(planet.items) == 0:
        #         break
        #     while len(planet.items) > 0:
        #         astronaut.backpack.append(planet.items.pop())
        #         astronaut.breathe()
        #         if astronaut.oxygen <= 0:
        #             explorers += 1
        #             break

        if len(planet.items) == 0:
            self.successful += 1
            return f"Planet: {planet_name} was explored. {explorers} astronauts participated in collecting items."
        self.unsuccessful += 1
        return "Mission is not completed."

    def find_astronauts_for_mission(self):
        return sorted([x for x in self.astronaut_repository.astronauts if x.oxygen > 30],
                      key=lambda x: x.oxygen,
                      reverse=True)[0:5]

    def report(self):
        result = ''
        result += f"{self.successful} successful missions!\n"
        result += f"{self.unsuccessful} missions were not completed!\n"
        result += "Astronauts' info:\n"
        for astronaut in self.astronaut_repository.astronauts:
            result += f"Name: {astronaut.name}\n"
            result += f"Oxygen: {astronaut.oxygen}\n"
            if len(astronaut.backpack) == 0:
                result += f"Backpack items: none\n"
            else:
                result += f"Backpack items: {', '.join(astronaut.backpack)}\n"
        return result.strip()




