from project.mammal import Mammal
from unittest import TestCase, main


class MammalTestCase(TestCase):
    def test_mammal_is_initialized_correctly(self):
        mammal = Mammal('Test', "cat", 'meow')
        self.assertEqual('Test', mammal.name)
        self.assertEqual('cat', mammal.type)
        self.assertEqual('meow', mammal.sound)
        self.assertEqual('animals', mammal._Mammal__kingdom)

    def test_make_sound(self):
        mammal = Mammal('Test', "cat", 'meow')
        result = 'Test makes meow'
        self.assertEqual(result, mammal.make_sound())

    def test_get_kingdom(self):
        mammal = Mammal('Test', "cat", 'meow')
        self.assertEqual('animals', mammal.get_kingdom())

    def test_info(self):
        mammal = Mammal('Test', "cat", 'meow')
        result = 'Test is of type cat'
        self.assertEqual(result, mammal.info())


if __name__ == '__main':
    main()
