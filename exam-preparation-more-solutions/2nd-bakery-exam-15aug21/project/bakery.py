from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        # if food_type in ["Bread", "Cake"]:
        food = self.__find_food_by_name(name)
        if food and food.__class__.__name__ == food_type:
            raise Exception(f"{food_type} {name} is already in the menu!")
        new_food = self.__create_new_food(name, price, food_type)
        self.food_menu.append(new_food)
        return f"Added {name} ({food_type}) to the food menu"

    def __find_food_by_name(self, name):
        for food in self.food_menu:
            if food.name == name:
                return food

    def __find_drink_by_name(self, name):
        for drink in self.drinks_menu:
            if drink.name == name:
                return drink

    def __create_new_food(self, name, price, food_type):
        food = None
        if food_type == 'Bread':
            food = Bread(name, price)
        if food_type == "Cake":
            food = Cake(name, price)
        return food

    def add_drink(self, drink_type: str, name: str, portion: float, brand:str):
        # if drink_type in ["Tea", "Water"]:
        drink = self.__find_drink_by_name(name)
        if drink and drink.__class__.__name__ == drink_type:
            raise Exception(f"{drink_type} {name} is already in the menu!")
        new_drink = self.__create_new_drink(name, portion, brand, drink_type)
        self.drinks_menu.append(new_drink)
        return f"Added {name} ({brand}) to the drink menu"

    def __create_new_drink(self, name, portion, brand, drink_type):
        drink = None
        if drink_type == "Tea":
            drink = Tea(name, portion, brand)
        if drink_type == "Water":
            drink = Water(name, portion, brand)
        return drink

    def __find_table_by_number(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table

    def __create_new_table(self, table_number, capacity, table_type):
        table = None
        if table_type == "InsideTable":
            table = InsideTable(table_number, capacity)
        if table_type == "OutsideTable":
            table = OutsideTable(table_number, capacity)
        return table

    def add_table(self, table_type: str, table_number: int, capacity: int):
        # if table_type in ["InsideTable", "OutsideTable"]:
        table = self.__find_table_by_number(table_number)
        if table:
            raise Exception(f"Table {table_number} is already in the bakery!")
        new_table = self.__create_new_table(table_number, capacity, table_type)
        self.tables_repository.append(new_table)
        return f"Added table number {table_number} in the bakery"

    def __find_free_table(self, number_of_people):
        for table in self.tables_repository:
            if table.capacity >= number_of_people and not table.is_reserved:
                return table

    def reserve_table(self, number_of_people: int):
        table = self.__find_free_table(number_of_people)
        if table:
            table.reserve(number_of_people)
            return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        table = self.__find_table_by_number(table_number)
        if not table:
            return f"Could not find table {table_number}"
        in_menu = []
        not_in_menu = []
        for name in food_names:
            food = self.__find_food_by_name(name)
            if food:
                in_menu.append(food)
                table.food_orders.append(food)
            else:
                not_in_menu.append(name)
        result = ''
        result += f"Table {table_number} ordered:\n"
        for f in in_menu:
            result += repr(f) + '\n'
        # if len(not_in_menu) > 0:
        result += f"{self.name} does not have in the menu:\n"
        for item in not_in_menu:
            result += item + '\n'

        return result.strip()

    def order_drink(self, table_number: int, *drink_names):
        table = self.__find_table_by_number(table_number)
        if not table:
            return f"Could not find table {table_number}"
        in_menu = []
        not_in_menu = []
        for name in drink_names:
            drink = self.__find_drink_by_name(name)
            if drink:
                in_menu.append(drink)
                table.drink_orders.append(drink)
            else:
                not_in_menu.append(name)
        result = ''
        result += f"Table {table_number} ordered:\n"
        for d in in_menu:
            result += repr(d) + '\n'
        # if len(not_in_menu) > 0:
        result += f"{self.name} does not have in the menu:\n"
        for item in not_in_menu:
            result += item + '\n'
        return result.strip()

    def leave_table(self, table_number: int):
        table = self.__find_table_by_number(table_number)
        if table:
            bill = table.get_bill()
            table.clear()
            self.total_income += bill
            result = f"Table: {table_number}" + '\n' + f"Bill: {bill:.2f}"
            return result

    def get_free_tables_info(self):
        result = ''
        for table in self.tables_repository:
            result += table.free_table_info() + '\n'
        return result.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
