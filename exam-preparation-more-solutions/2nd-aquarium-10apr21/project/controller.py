from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in ["FreshwaterAquarium", "SaltwaterAquarium"]:
            return "Invalid aquarium type."
        if aquarium_type == "FreshwaterAquarium":
            new_aquarium = FreshwaterAquarium(aquarium_name)
            self.aquariums.append(new_aquarium)
            return f"Successfully added {aquarium_type}."
        if aquarium_type == "SaltwaterAquarium":
            new_aquarium = SaltwaterAquarium(aquarium_name)
            self.aquariums.append(new_aquarium)
            return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in ["Ornament", "Plant"]:
            return "Invalid decoration type."
        if decoration_type == "Ornament":
            new_dec = Ornament()
            self.decorations_repository.add(new_dec)
            return f"Successfully added {decoration_type}."
        if decoration_type == "Plant":
            new_dec = Plant()
            self.decorations_repository.add(new_dec)
            return f"Successfully added {decoration_type}."

    def __find_decoration_by_type(self, decoration_type):
        for decoration in self.decorations_repository.decorations:
            if decoration.__class__.__name__ == decoration_type:
                return decoration

    def __find_aquarium_by_name(self, name):
        for aq in self.aquariums:
            if aq.name == name:
                return aq

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.__find_decoration_by_type(decoration_type)
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        if decoration and aquarium:
            self.decorations_repository.remove(decoration)
            aquarium.add_decoration(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."
        if not decoration:
            return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in ["FreshwaterFish", "SaltwaterFish"]:
            return f"There isn't a fish of type {fish_type}."
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        if aquarium.__class__.__name__ == "FreshwaterAquarium" and fish_type == "SaltwaterFish":
            return "Water not suitable."
        if aquarium.__class__.__name__ == "SaltwaterAquarium" and fish_type == "FreshwaterFish":
            return "Water not suitable."
        if len(aquarium.fish) == aquarium.capacity:
            return "Not enough capacity."

        if aquarium.__class__.__name__ == "FreshwaterAquarium" and fish_type == "FreshwaterFish":
            new_fish = FreshwaterFish(fish_name, fish_species, price)
            aquarium.fish.append(new_fish)
            return f"Successfully added {fish_type} to {aquarium_name}."
        if aquarium.__class__.__name__ == "SaltwaterAquarium" and fish_type == "SaltwaterFish":
            new_fish = SaltwaterFish(fish_name, fish_species, price)
            aquarium.fish.append(new_fish)
            return f"Successfully added {fish_type} to {aquarium_name}."

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        aquarium.feed()
        count = len(aquarium.fish)
        return f"Fish fed: {count}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        value = 0
        value += sum([f.price for f in aquarium.fish])
        value += sum([d.price for d in aquarium.decorations])
        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        result = ''
        for aquarium in self.aquariums:
            result += str(aquarium)
        return result.strip()
