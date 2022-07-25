from project.drink.tea import Tea
from project.drink.water import Water


class DrinkFactory:
    food_types = {
        "Tea": Tea,
        "Water": Water
    }

    def create_drink(self, drink_type, name, portion, brand):
        return self.__class__.food_types[drink_type](name, portion, brand)
