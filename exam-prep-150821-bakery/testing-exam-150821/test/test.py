from unittest import main, TestCase
from project.pet_shop import PetShop


class PetShopTests(TestCase):
    def setUp(self) -> None:
        self.shop = PetShop('test')

    def test_is_initialized_correctly(self):
        shop = PetShop('test')
        self.assertEqual('test', shop.name)
        self.assertEqual({}, shop.food)
        self.assertEqual([], shop.pets)

    def test_add_food_if_quantity_is_zero_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.shop.add_food('name', 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_if_quantity_is_neg_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.shop.add_food('name', -1)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_new_food_key_is_added(self):
        result = self.shop.add_food('new', 1)
        self.assertTrue('new' in self.shop.food)
        self.assertEqual(1, self.shop.food['new'])
        self.assertEqual("Successfully added 1.00 grams of new.", result)

    def test_add_food_to_existing_key(self):
        self.shop.food['food'] = 2
        result = self.shop.add_food('food', 1)
        self.assertEqual(3, self.shop.food['food'])
        self.assertTrue('food' in self.shop.food)
        self.assertEqual("Successfully added 1.00 grams of food.", result)

    def test_add_pet_which_exists_raises(self):
        self.shop.pets.append('dog')
        with self.assertRaises(Exception) as ex:
            self.shop.add_pet('dog')
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_add_pet_new_pet(self):
        result = self.shop.add_pet('bunny')
        self.assertTrue('bunny' in self.shop.pets)
        self.assertEqual("Successfully added bunny.", result)

    def test_feed_not_existing_pet_raises(self):
        # self.shop.pets = ['dog', 'cat']
        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet('name', 'bunny')
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_not_existing_food_raises(self):
        self.shop.pets.append('bunny')
        result = self.shop.feed_pet('new', 'bunny')
        # self.assertFalse('new' in self.shop.food)
        self.assertEqual('You do not have new', result)

    def test_feed_pets_with_less_than_100_grams(self):
        self.shop.pets.append('dog')
        self.shop.food['food'] = 10
        result = self.shop.feed_pet('food', 'dog')
        self.assertEqual(1010.00, self.shop.food['food'])
        self.assertEqual("Adding food...", result)

    def test_feed_pet_food_that_is_enough(self):
        self.shop.pets.append('dog')
        self.shop.food['food'] = 1000
        result = self.shop.feed_pet('food', 'dog')
        self.assertEqual(900, self.shop.food['food'])
        self.assertEqual("dog was successfully fed", result)

    def test_repr_method(self):
        self.shop.pets.append('dog')
        self.shop.pets.append('cat')
        result = repr(self.shop)
        self.assertEqual(f'Shop test:\nPets: dog, cat', result)


if __name__ == '__main__':
    main()
