from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        comfort = sum(d.comfort for d in self.decorations)
        return comfort

    def add_fish(self, fish: object):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."
        if fish.__class__.__name__ == "FreshwaterFish" and self.__class__.__name__ == "FreshwaterAquarium":
            self.fish.append(fish)
            return f"Successfully added FreshwaterFish to {self.name}."
        if fish.__class__.__name__ == "SaltwaterFish" and self.__class__.__name__ == "SaltwaterAquarium":
            self.fish.append(fish)
            return f"Successfully added SaltwaterFish to {self.name}."

    def remove_fish(self, fish: object):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration: object):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = f'{self.name}:\n'
        if len(self.fish) == 0:
            result += f"Fish: none\n"
        else:
            result += f"Fish: {' '.join(f.name for f in self.fish)}\n"
        result += f"Decorations: {len(self.decorations)}\n"
        result += f"Comfort: {self.calculate_comfort()}\n"
        return result
