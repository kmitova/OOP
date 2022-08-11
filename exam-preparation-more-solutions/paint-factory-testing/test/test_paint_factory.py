from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class PaintFactoryTests(TestCase):
    def test_init_is_correct(self):
        pf = PaintFactory("test", 100)
        self.assertEqual('test', pf.name)
        self.assertEqual({}, pf.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], pf.valid_ingredients)

    def test_add_ing_valid_ing_has_space(self):
        pf = PaintFactory("test", 100)
        self.assertEqual({}, pf.ingredients)
        pf.add_ingredient('white', 20)
        self.assertEqual({'white': 20}, pf.ingredients)

    def test_add_ing_valid_ing_no_space(self):
        pf = PaintFactory("test", 100)
        self.assertEqual({}, pf.ingredients)
        with self.assertRaises(ValueError) as ex:
            pf.add_ingredient('white', 200)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_add_ing_invalid_ing(self):
        pf = PaintFactory("test", 100)
        self.assertEqual({}, pf.ingredients)
        with self.assertRaises(TypeError) as ex:
            pf.add_ingredient('invalid', 20)
        self.assertEqual("Ingredient of type invalid not allowed in PaintFactory", str(ex.exception))

    def test_remove_valid_ing_valid_qty(self):
        pf = PaintFactory("test", 100)
        self.assertEqual({}, pf.ingredients)
        pf.add_ingredient('white', 20)
        pf.remove_ingredient('white', 10)
        self.assertEqual({"white": 10}, pf.ingredients)

    def test_remove_valid_ing_invalid_qty(self):
        pf = PaintFactory("test", 100)
        self.assertEqual({}, pf.ingredients)
        pf.add_ingredient('white', 20)
        with self.assertRaises(ValueError) as ex:
            pf.remove_ingredient('white', 30)
        self.assertEqual({"white": 20}, pf.ingredients)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_invalid_ing(self):
        pf = PaintFactory("test", 100)
        # self.assertEqual({}, pf.ingredients)
        # pf.add_ingredient('white', 20)
        with self.assertRaises(KeyError) as ex:
            pf.remove_ingredient('invalid', 30)

        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))
        # def test_remove_ing_not_valid_raises(self):

    def test_products_prop(self):
        factory = PaintFactory('name', 100)
        factory.add_ingredient("white", 2)
        self.assertEqual({"white": 2}, factory.products)


if __name__ == '__main__':
    main()