from project.animals.animal import Mammal


class Mouse(Mammal):
    ALLOWED_FOOD = ['Fruit', 'Vegetable']
    WEIGHT_INCREMENT = 0.1

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Squeak'


class Dog(Mammal):
    ALLOWED_FOOD = ['Meat']
    WEIGHT_INCREMENT = 0.4

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Woof!'


class Cat(Mammal):
    ALLOWED_FOOD = ['Meat', 'Vegetable']
    WEIGHT_INCREMENT = 0.3

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Meow'


class Tiger(Mammal):
    ALLOWED_FOOD = ['Meat']
    WEIGHT_INCREMENT = 1

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'ROAR!!!'


