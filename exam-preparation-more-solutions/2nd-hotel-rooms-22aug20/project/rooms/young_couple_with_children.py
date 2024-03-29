from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, name: str, salary_one: float, salary_two: float, *children):
        count = len(children) + 2
        super().__init__(name, salary_one + salary_two, count)
        self.room_cost = 30
        self.children = list(children)
        self.appliances = [TV(), Fridge(), Laptop()] * count
        self.calculate_expenses(self.appliances, self.children)
        # self.members = len(children) + 2
