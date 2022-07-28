from project_testing.plantation import Plantation
from unittest import main, TestCase


class PlantationTests(TestCase):
    def test_init(self):
        plantation = Plantation(200)
        self.assertEqual(200, plantation.size)
        self.assertEqual({}, plantation.plants)
        self.assertEqual([], plantation.workers)

    def test_size_prop(self):
        plantation = Plantation(200)
        self.assertEqual(200, plantation._Plantation__size)

    def test_size_setter_happy_case(self):
        plantation = Plantation(200)
        plantation.size = 2
        self.assertEqual(2, plantation._Plantation__size)

    def test_name_setter_raises(self):
        plantation = Plantation(200)
        with self.assertRaises(ValueError) as ex:
            plantation.size = -1
        self.assertEqual("Size must be positive number!", str(ex.exception))

    def test_hire_worker(self):
        plantation = Plantation(200)
        result = plantation.hire_worker("Kelly")
        self.assertTrue("Kelly" in plantation.workers)
        self.assertEqual("Kelly successfully hired.", result)
        self.assertTrue(len(plantation.workers) == 1)

    def test_hire_raises(self):
        plantation = Plantation(200)
        plantation.hire_worker("Kelly")
        # plantation.workers = ["Kelly"]
        with self.assertRaises(ValueError) as ex:
            plantation.hire_worker("Kelly")
        self.assertEqual("Worker already hired!", str(ex.exception))
        self.assertTrue(len(plantation.workers) == 1)

    def test_len_method(self):
        plantation = Plantation(200)
        plantation.hire_worker("Kelly")
        plantation.planting("Kelly", "plant")
        # plantation.planting("Kelly", 'plant2')
        plantation.hire_worker("Jack")
        plantation.planting("Jack", "plant2")
        result = len(plantation)
        self.assertEqual(2, result)

    def test_planting_no_worker_raises(self):
        plantation = Plantation(200)
        with self.assertRaises(ValueError) as ex:
            plantation.planting("Kelly", "plant")
        self.assertEqual("Worker with name Kelly is not hired!", str(ex.exception))

    def test_planting_if_worker_has_planted(self):
        plantation = Plantation(200)
        plantation.hire_worker("Kelly")
        self.assertTrue("Kelly" in plantation.workers)
        plantation.planting("Kelly", "plant")
        # plantation.planting("Kelly", "plant2")
        result = plantation.planting("Kelly", "plant2")
        # print(plantation.plants)
        # self.assertTrue('plant2' in plantation.workers["Kelly"])

        self.assertTrue(len(plantation.plants) == 1)
        self.assertEqual("Kelly planted plant2.", result)

    def test_planting_full_raises(self):
        plantation = Plantation(2)
        plantation.hire_worker("Kelly")
        self.assertTrue("Kelly" in plantation.workers)
        plantation.planting("Kelly", "plant")
        plantation.planting("Kelly", "plant2")
        with self.assertRaises(ValueError) as ex:
            # result = len(plantation) >= plantation.size
            plantation.planting("Kelly", "plant3")
        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_planting_first_plant(self):
        plantation = Plantation(2)
        plantation.hire_worker("Kelly")
        self.assertTrue("Kelly" in plantation.workers)
        result = plantation.planting("Kelly", "plant")
        self.assertEqual("Kelly planted it's first plant.", result)

    def test_str_method(self):
        plantation = Plantation(2)
        plantation.hire_worker("Kelly")
        plantation.planting("Kelly", "plant")
        plantation.hire_worker("Jack")
        plantation.planting("Jack", "plant")

        result = str(plantation)
        expected = "Plantation size: 2" + '\n' + "Kelly, Jack" + "\n" + "Kelly planted: plant" + '\n' + "Jack planted: plant"
        self.assertEqual(expected, result)

    def test_repr_method(self):
        plantation = Plantation(2)
        plantation.hire_worker("Kelly")
        plantation.hire_worker("Jack")
        result = repr(plantation)
        expected = 'Size: 2\nWorkers: Kelly, Jack'
        self.assertEqual(expected, result)












if __name__ == "__main__":
    main()
