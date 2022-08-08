from project.plantation import Plantation
from unittest import TestCase, main


class PlantationTests(TestCase):
    def test_init_is_correct(self):
        plantation = Plantation(100)
        self.assertEqual(100, plantation.size)
        self.assertEqual({}, plantation.plants)
        self.assertEqual([], plantation.workers)

    def test_size_setter_invalid_raises(self):
        plantation = Plantation(100)
        with self.assertRaises(ValueError) as ex:
            plantation.size = -1
        self.assertEqual("Size must be positive number!", str(ex.exception))

    def test_hire_worker_already_hired_raises(self):
        plantation = Plantation(100)
        plantation.workers = ['worker1']
        with self.assertRaises(ValueError) as ex:
            plantation.hire_worker('worker1')
        self.assertEqual("Worker already hired!", str(ex.exception))

    def test_hire_worker_happy_case(self):
        plantation = Plantation(100)
        self.assertEqual([], plantation.workers)
        self.assertEqual(0, len(plantation.workers))
        result = plantation.hire_worker('worker1')
        self.assertEqual("worker1 successfully hired.", result)
        self.assertEqual(['worker1'], plantation.workers)
        self.assertEqual(1, len(plantation.workers))

    def test_length_method(self):
        plantation = Plantation(100)
        result = len(plantation)
        self.assertEqual(0, result)

    def test_planting_with_non_existing_worker(self):
        plantation = Plantation(100)
        with self.assertRaises(ValueError) as ex:
            plantation.planting('worker1', 'plant1')
        self.assertEqual("Worker with name worker1 is not hired!", str(ex.exception))

    def test_planting_full_size_raises(self):
        plantation = Plantation(0)
        plantation.hire_worker('worker1')
        with self.assertRaises(ValueError) as ex:
            plantation.planting("worker1", 'plant1')
        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_planting_first_plant(self):
        plantation = Plantation(10)
        plantation.hire_worker('worker1')
        result = plantation.planting("worker1", 'plant1')
        self.assertEqual("worker1 planted it's first plant1.", result)
        self.assertEqual(1, len(plantation.plants))
        self.assertTrue('worker1' in plantation.plants)
        self.assertTrue('plant1' in plantation.plants['worker1'])

    def test_planting_old_worker(self):
        plantation = Plantation(10)
        plantation.hire_worker('worker1')
        plantation.planting("worker1", 'plant1')
        result = plantation.planting("worker1", 'plant2')
        self.assertEqual("worker1 planted plant2.", result)
        self.assertEqual(1, len(plantation.plants))
        self.assertTrue('worker1' in plantation.plants)
        self.assertTrue('plant1' in plantation.plants['worker1'])
        self.assertTrue('plant2' in plantation.plants['worker1'])

    def test_str_method(self):
        plantation = Plantation(10)
        plantation.hire_worker('worker1')
        plantation.hire_worker('worker2')
        plantation.planting("worker1", 'plant1')
        plantation.planting("worker2", 'plant2')
        result = str(plantation)
        expected = f"Plantation size: 10\nworker1, worker2\nworker1 planted: plant1\nworker2 planted: plant2"
        self.assertEqual(expected, result)

    def test_repr_method(self):
        plantation = Plantation(10)
        plantation.hire_worker('worker1')
        plantation.hire_worker('worker2')
        result = repr(plantation)
        expected = "Size: 10\nWorkers: worker1, worker2"
        self.assertEqual(expected, result)

    # old tests (without it 93/100)
    def test_len_method(self):
        plantation = Plantation(200)
        plantation.hire_worker("Kelly")
        plantation.planting("Kelly", "plant")
        # plantation.planting("Kelly", 'plant2')
        plantation.hire_worker("Jack")
        plantation.planting("Jack", "plant2")
        result = len(plantation)
        self.assertEqual(2, result)

if __name__ == '__main__':
    main()