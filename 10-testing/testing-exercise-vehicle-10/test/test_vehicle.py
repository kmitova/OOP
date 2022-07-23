from project.vehicle import Vehicle
from unittest import TestCase, main


class VehicleTests(TestCase):
    def test_is_initialized_correctly(self):
        vehicle = Vehicle(10, 200)
        self.assertEqual(10, vehicle.fuel)
        self.assertEqual(200, vehicle.horse_power)
        self.assertEqual(10, vehicle.capacity)
        self.assertEqual(1.25, vehicle.fuel_consumption)

    def test_drive_if_fuel_is_less_than_needed_raises(self):
        vehicle = Vehicle(10, 200)
        with self.assertRaises(Exception) as ex:
            vehicle.drive(20000)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_if_needed_fuel_is_enough(self):
        vehicle = Vehicle(20, 200)
        vehicle.drive(10)
        self.assertEqual(7.5, vehicle.fuel)

    def test_refuel_if_fuel_more_than_capacity_raises(self):
        vehicle = Vehicle(20, 200)
        with self.assertRaises(Exception) as ex:
            vehicle.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_if_capacity_is_available(self):
        vehicle = Vehicle(20, 200)
        vehicle.drive(10)
        vehicle.refuel(5)
        self.assertEqual(12.5, vehicle.fuel)

    def test_str_method(self):
        vehicle = Vehicle(20, 200)
        expected_result = "The vehicle has 200 " \
               "horse power with 20 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected_result, str(vehicle))


if __name__ == '__main__':
    main()


