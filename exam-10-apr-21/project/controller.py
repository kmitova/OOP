from exam.project.aquarium.freshwater_aquarium import FreshwaterAquarium
from exam.project.aquarium.saltwater_aquarium import SaltwaterAquarium
from exam.project.decoration.decoration_repository import DecorationRepository
from exam.project.decoration.ornament import Ornament
from exam.project.decoration.plant import Plant
from exam.project.fish.freshwater_fish import FreshwaterFish
from exam.project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == 'FreshwaterAquarium':
            aquarium = FreshwaterAquarium(aquarium_name)
            self.aquariums.append(aquarium)
            return f"Successfully added {aquarium_type}."
        if aquarium_type == "SaltwaterAquarium":
            aquarium = SaltwaterAquarium(aquarium_name)
            self.aquariums.append(aquarium)
            return f"Successfully added {aquarium_type}."
        return "Invalid aquarium type."

    def add_decoration(self, decoration_type: str):
        if decoration_type == "Ornament":
            decoration = Ornament()
            self.decorations_repository.add(decoration)
            return f"Successfully added {decoration_type}."
        if decoration_type == "Plant":
            decoration = Plant()
            self.decorations_repository.add(decoration)
            return f"Successfully added {decoration_type}."
        return "Invalid decoration type."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                for decoration in self.decorations_repository.decorations:
                    if decoration.__class__.__name__ == decoration_type:
                        aquarium.add_decoration(decoration)
                        self.decorations_repository.remove(decoration)
                        return f"Successfully added {decoration_type} to {aquarium_name}."
                return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in ["SaltwaterFish", "FreshwaterFish"]:
            return f"There isn't a fish of type {fish_type}."
        fish = None
        if fish_type == "FreshwaterFish":
            fish = FreshwaterFish(fish_name, fish_species, price)
        if fish_type == "SaltwaterFish":
            fish = SaltwaterFish(fish_name, fish_species, price)
        aquarium = None
        for a in self.aquariums:
            if a.name == aquarium_name:
                aquarium = a
                break
        if aquarium.__class__.__name__ == "FreshwaterAquarium" and fish_type == "SaltwaterFish":
            return "Water not suitable."
        if aquarium.__class__.__name__ == "SaltwaterAquarium" and fish_type == "FreshwaterFish":
            return "Water not suitable."
        return aquarium.add_fish(fish)
        # if len(aquarium.fish) == aquarium.capacity:
        #     return "Not enough capacity."

        # aquarium.fish.append(fish)
        # return f"Successfully added {fish_type} to {aquarium_name}."

    def feed_fish(self, aquarium_name: str):
        fed = 0
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                aquarium.feed()
                fed = len(aquarium.fish)
                # for fish in aquarium.fish:
                #     fish.eat()
        return f"Fish fed: {fed}"

    def calculate_value(self, aquarium_name: str):
        dec_value = 0
        fish_value = 0
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                for dec in aquarium.decorations:
                    dec_value += dec.price
                for fish in aquarium.fish:
                    fish_value += fish.price
        total = dec_value + fish_value
        return f"The value of Aquarium {aquarium_name} is {total:.2f}."

    def report(self):
        result = ''
        for aquarium in self.aquariums:
            result += str(aquarium)
        return result


