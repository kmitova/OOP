from unittest import TestCase, main
from project.factory.paint_factory import PaintFactory


class PaintFactoryTests(TestCase):
    def test_init_is_correct(self):
        factory = PaintFactory('name', 100)
        self.assertEqual('name', factory.name)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], factory.valid_ingredients)
        self.assertEqual({}, factory.ingredients)

    def test_add_invalid_ingredient_raises(self):
        factory = PaintFactory('name', 100)
        with self.assertRaises(TypeError) as ex:
            factory.add_ingredient('invalid', 10)
        self.assertEqual("Ingredient of type invalid not allowed in PaintFactory", str(ex.exception))

    def test_add_ingredient_over_capacity_raises(self):
        factory = PaintFactory('name', 100)
        with self.assertRaises(ValueError) as ex:
            factory.add_ingredient('white', 102)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_add_valid_ing_and_qty_not_yet_added(self):
        factory = PaintFactory('name', 100)
        factory.add_ingredient('white', 10)
        self.assertTrue(len(factory.ingredients) == 1)
        self.assertEqual(10, factory.ingredients['white'])
        self.assertEqual({'white': 10}, factory.ingredients)

    def test_add_valid_ing_and_qty_already_in_dict(self):
        factory = PaintFactory('name', 100)
        factory.add_ingredient('white', 10)
        self.assertTrue(len(factory.ingredients) == 1)
        self.assertEqual(10, factory.ingredients['white'])
        factory.add_ingredient('white', 10)
        self.assertTrue(len(factory.ingredients) == 1)
        self.assertEqual(20, factory.ingredients['white'])

    def test_remove_ingredient_invalid_product_type_raises(self):
        factory = PaintFactory('name', 100)
        with self.assertRaises(KeyError) as ex:
            factory.remove_ingredient("purple", 2)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))
    # def test_remove_ing_not_valid_raises(self):
    #     factory = PaintFactory('name', 100)
    #     factory.add_ingredient('white', 10)
    #
    #     with self.assertRaises(KeyError) as ex:
    #         factory.remove_ingredient('red', 10)
    #     self.assertEqual("No such ingredient in the factory", str(ex.exception))

    def test_remove_ing_invalid_qty_raises(self):
        factory = PaintFactory('name', 100)
        factory.add_ingredient('white', 10)
        with self.assertRaises(ValueError) as ex:
            factory.remove_ingredient('white', 20)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_ing_valid(self):
        factory = PaintFactory('name', 100)
        factory.add_ingredient('white', 10)
        factory.remove_ingredient('white', 9)
        self.assertEqual(1, factory.ingredients['white'])

    def test_repr_method(self):
        factory = PaintFactory('name', 100)
        factory.add_ingredient('white', 10)
        result = repr(factory)
        expected = "Factory name: name with capacity 100.\nwhite: 10\n"
        self.assertEqual(expected, result)

    def test_can_add(self):
        factory = PaintFactory('name', 100)
        factory.add_ingredient('white', 10)
        self.assertTrue(factory.can_add(30))
        self.assertFalse(factory.can_add(150))

    def test_product_prop(self):
        factory = PaintFactory('name', 100)
        factory.add_ingredient("white", 2)
        self.assertEqual({"white": 2}, factory.products)


if __name__ == '__main__':
    main()