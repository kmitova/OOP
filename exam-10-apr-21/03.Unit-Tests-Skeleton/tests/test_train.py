from exam.project import Train
from unittest import TestCase, main


class TrainTests(TestCase):
    def test_init_works(self):
        train = Train('test', 200)
        self.assertEqual('test', train.name)
        self.assertEqual(200, train.capacity)
        self.assertEqual([], train.passengers)

    def test_add_passengers_if_capacity_full_raises(self):
        train = Train('test', 1)
        train.add("Kelly")

        with self.assertRaises(ValueError) as ex:
            train.add("Jack")
        self.assertEqual("Train is full", str(ex.exception))

    def test_add_existing_passenger(self):
        train = Train('test', 2)
        train.add("Kelly")
        with self.assertRaises(ValueError) as ex:
            train.add("Kelly")
        self.assertEqual("Passenger Kelly Exists", str(ex.exception))

    def test_add_passenger_happy_case(self):
        train = Train('test', 2)
        result = train.add("Kelly")
        self.assertTrue("Kelly" in train.passengers)
        self.assertEqual("Added passenger Kelly", result)

    def test_remove_not_existing_passenger_raises(self):
        train = Train('test', 2)
        train.add("Kelly")
        with self.assertRaises(ValueError) as ex:
            train.remove("Jack")
        self.assertEqual("Passenger Not Found", str(ex.exception))
        self.assertFalse("Jack" in train.passengers)

    def test_remove_passenger_happy_case(self):
        train = Train('test', 2)
        train.add("Kelly")
        train.add("Jack")
        result = train.remove("Jack")
        self.assertFalse("Jack" in train.passengers)
        self.assertTrue("Kelly" in train.passengers)
        self.assertEqual("Removed Jack", result)


if __name__ == '__main__':
    main()

