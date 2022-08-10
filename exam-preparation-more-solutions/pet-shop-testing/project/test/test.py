from project.pet_shop import PetShop
from unittest import main, TestCase


class PetShopTests(TestCase):
    def tests_init_is_correct(self):
        shop = PetShop('test')
        self.assertEqual('test', shop.name)
        self.assertEqual({}, shop.food)
        self.assertEqual([], shop.pets)

    def test_add_food_neg_qty_raises(self):
        shop = PetShop('test')
        with self.assertRaises(ValueError) as ex:
            shop.add_food('dog food', -300)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_zero_qty_raises(self):
        shop = PetShop('test')
        with self.assertRaises(ValueError) as ex:
            shop.add_food('dog food', 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_new_food(self):
        shop = PetShop('test')
        result = shop.add_food('dog food', 100)
        self.assertEqual(1, len(shop.food))
        self.assertEqual({'dog food': 100}, shop.food)
        self.assertEqual("Successfully added 100.00 grams of dog food.", result)

    def test_add_food_existing(self):
        shop = PetShop('test')
        shop.add_food('dog food', 100)
        self.assertEqual(1, len(shop.food))
        self.assertEqual({'dog food': 100}, shop.food)
        result = shop.add_food('dog food', 100)
        self.assertEqual(1, len(shop.food))
        self.assertEqual({'dog food': 200}, shop.food)
        self.assertEqual("Successfully added 100.00 grams of dog food.", result)

    def test_add_pet_new_pet(self):
        shop = PetShop('test')
        self.assertEqual(0, len(shop.pets))
        result = shop.add_pet('dog')
        self.assertEqual(1, len(shop.pets))
        self.assertTrue('dog' in shop.pets)
        self.assertEqual("Successfully added dog.", result)

    def test_add_existing_pet_raises(self):
        shop = PetShop('test')
        self.assertEqual(0, len(shop.pets))
        shop.add_pet('dog')
        with self.assertRaises(Exception) as ex:
            shop.add_pet('dog')
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_pet_invalid_pet_raises(self):
        shop = PetShop('test')
        shop.add_food('dog food', 100)
        self.assertEqual(0, len(shop.pets))
        with self.assertRaises(Exception) as ex:
            shop.feed_pet('dog food', 'dog')
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_invalid_food(self):
        shop = PetShop('test')
        shop.add_pet('dog')
        result = shop.feed_pet('dog food', 'dog')
        self.assertEqual('You do not have dog food', result)

    def test_feed_pet_less_than_100gr_food(self):
        shop = PetShop('test')
        shop.add_food('dog food', 10)
        shop.add_pet('dog')
        result = shop.feed_pet('dog food', 'dog')
        self.assertEqual({'dog food': 1010.00}, shop.food)
        self.assertEqual("Adding food...", result)

    def test_feed_pet_all_valid(self):
        shop = PetShop('test')
        shop.add_food('dog food', 1000)
        shop.add_pet('dog')
        result = shop.feed_pet('dog food', 'dog')
        self.assertEqual({'dog food': 900}, shop.food)
        self.assertEqual("dog was successfully fed", result)

    def test_repr(self):
        shop = PetShop('test')
        shop.add_food('dog food', 1000)
        shop.add_pet('dog')
        shop.add_pet('cat')
        expected = "Shop test:\nPets: dog, cat"
        result = repr(shop)
        self.assertEqual(expected, result)





if __name__ == "__main__":
    main()
