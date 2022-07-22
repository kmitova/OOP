class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


# car = Car("a", "b", 1, 4)
# car.make = ""
# print(car)
#

from unittest import TestCase, main

class CarTests(TestCase):
    def test_is_initialized_correctly(self):
        car1 = Car("a", "b", 1, 4)
        self.assertEqual("a", car1.make)
        self.assertEqual("b", car1.model)
        self.assertEqual(1, car1.fuel_consumption)
        self.assertEqual(4, car1.fuel_capacity)
        self.assertEqual(0, car1.fuel_amount)

    def test_make_property(self):
        car1 = Car("a", "b", 1, 4)
        car1.make = "b"
        self.assertEqual("b", car1._Car__make)

    def test_make_setter_raises_if_empty(self):
        car1 = Car("a", "b", 1, 4)
        with self.assertRaises(Exception) as ex:
            car1.make = None
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_make_setter_returns_correct_new_value_of_make(self):
        car1 = Car("a", "b", 1, 4)
        car1.make = "c"
        self.assertEqual("c", car1._Car__make)

    def test_model_property(self):
        car1 = Car("a", "b", 1, 4)
        car1.model = "d"
        self.assertEqual("d", car1._Car__model)

    def test_model_setter_raises_if_empty(self):
        car1 = Car("a", "b", 1, 4)
        with self.assertRaises(Exception) as ex:
            car1.model = None
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_model_setter_returns_correct_new_value_of_make(self):
        car1 = Car("a", "b", 1, 4)
        car1.model = "c"
        self.assertEqual("c", car1._Car__model)

    def test_fuel_consumption_property(self):
        car1 = Car("a", "b", 1, 4)
        car1.fuel_consumption = 3
        self.assertEqual(3, car1._Car__fuel_consumption)

    def test_fuel_consumption_zero_setter_raises(self):
        car1 = Car("a", "b", 1, 4)
        with self.assertRaises(Exception) as ex:
            car1.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_negative_setter_raises(self):
        car1 = Car("a", "b", 1, 4)
        with self.assertRaises(Exception) as ex:
            car1.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_valid_data_setter(self):
        car1 = Car("a", "b", 1, 4)
        car1.fuel_consumption = 4
        self.assertEqual(4, car1._Car__fuel_consumption)

    def test_fuel_capacity_property(self):
        car1 = Car("a", "b", 1, 4)
        car1.fuel_capacity = 3
        self.assertEqual(3, car1._Car__fuel_capacity)

    def test_fuel_capacity_zero_setter_raises(self):
        car1 = Car("a", "b", 1, 4)
        with self.assertRaises(Exception) as ex:
            car1.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_negative_setter_raises(self):
        car1 = Car("a", "b", 1, 4)
        with self.assertRaises(Exception) as ex:
            car1.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_valid_data_setter(self):
        car1 = Car("a", "b", 1, 4)
        car1.fuel_capacity = 4
        self.assertEqual(4, car1._Car__fuel_capacity)

    def test_fuel_amount_property(self):
        car1 = Car("a", "b", 1, 4)
        car1.fuel_amount = 3
        self.assertEqual(3, car1.fuel_amount)

    def test_fuel_amount_negative_setter_raises(self):
        car1 = Car("a", "b", 1, 4)
        with self.assertRaises(Exception) as ex:
            car1.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_fuel_amount_valid_data_setter(self):
        car1 = Car("a", "b", 1, 4)
        car1.fuel_amount = 4
        self.assertEqual(4, car1.fuel_amount)

    def test_refuel_negative_amount_raises(self):
        car1 = Car("a", "b", 1, 4)
        with self.assertRaises(Exception) as ex:
            car1.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_zero_amount_raises(self):
        car1 = Car("a", "b", 1, 4)
        with self.assertRaises(Exception) as ex:
            car1.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_valid_data(self):
        car1 = Car("a", "b", 1, 4)
        car1.refuel(1)
        self.assertEqual(1, car1.fuel_amount)

    def test_check_if_fuel_amount_is_more_than_capacity(self):
        car1 = Car("a", "b", 1, 4)
        car1.refuel(1)
        self.assertFalse(car1.fuel_amount > car1._Car__fuel_capacity)
        car1.refuel(11)
        self.assertEqual(4, car1.fuel_amount)
        # self.assertFalse(car1.fuel_amount > car1._Car__fuel_capacity)

    def test_if_needed_fuel_is_enough(self):
        car1 = Car("a", "b", 1, 4)
        car1.refuel(1)
        car1.drive(50)
        self.assertEqual(0.5, car1._Car__fuel_amount)

    def test_if_needed_fuel_is_not_enough_raises(self):
        car1 = Car("a", "b", 1, 4)
        car1.refuel(1)
        with self.assertRaises(Exception) as ex:
            car1.drive(1000)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == '__main__':
    main()
