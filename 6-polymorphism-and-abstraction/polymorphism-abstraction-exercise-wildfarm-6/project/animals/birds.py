from project.animals.animal import Bird


class Hen(Bird):
    ALLOWED_FOOD = ['Fruit', 'Vegetable', 'Meat', 'Seed']
    WEIGHT_INCREMENT = 0.35

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return 'Cluck'


class Owl(Bird):
    ALLOWED_FOOD = ['Meat']
    WEIGHT_INCREMENT = 0.25

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return 'Hoot Hoot'


