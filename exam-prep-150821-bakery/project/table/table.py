from abc import ABC, abstractmethod
from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    @abstractmethod
    def min_table_number(self):
        pass

    @property
    @abstractmethod
    def max_table_number(self):
        pass

    @property
    @abstractmethod
    def table_number_error(self):
        pass

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if value < self.min_table_number or value > self.max_table_number:
            raise ValueError(self.table_number_error)
        self.__table_number = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self.__capacity = value

    def reserve(self, number_of_people):
        self.is_reserved = True
        self.number_of_people += number_of_people

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        bill = 0
        for drink in self.drink_orders:
            bill += drink.price
        for food in self.food_orders:
            bill += food.price
        return bill

    def clear(self):
        self.number_of_people = 0
        self.food_orders = []
        self.drink_orders = []
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            result = f"Table: {self.table_number}\nType: {self.__class__.__name__}\nCapacity: {self.capacity}"
            return result

