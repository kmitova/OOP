from unittest import TestCase, main
from project.train.train import Train


class TrainTests(TestCase):
    def test_init_correct(self):
        train = Train('test', 100)
        self.assertEqual('test', train.name)
        self.assertEqual(100, train.capacity)
        self.assertEqual([], train.passengers)

    def test_add_full_train_raises(self):
        train = Train('test', 1)
        train.add('name')
        with self.assertRaises(ValueError) as ex:
            train.add('name2')
        self.assertEqual("Train is full", str(ex.exception))

    def test_add_existing_raises(self):
        train = Train('test', 5)
        train.add('name')
        with self.assertRaises(ValueError) as ex:
            train.add('name')
        self.assertEqual("Passenger name Exists", str(ex.exception))

    def test_add_passenger_valid(self):
        train = Train('test', 5)
        result = train.add('name')
        self.assertEqual(1, len(train.passengers))
        self.assertTrue('name' in train.passengers)
        self.assertEqual("Added passenger name", result)

    def test_remove_invalid_passenger_raises(self):
        train = Train('test', 5)
        train.add('name1')
        with self.assertRaises(ValueError) as ex:
            train.remove('name2')
        self.assertEqual("Passenger Not Found", str(ex.exception))
        self.assertEqual(1, len(train.passengers))

    def test_remove_valid(self):
        train = Train('test', 5)
        train.add('name')
        result = train.remove('name')
        self.assertTrue(len(train.passengers) == 0)
        self.assertEqual("Removed name", result)





if __name__ == '__main__':
    main()