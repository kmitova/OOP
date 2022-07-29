from project.movie import Movie
from unittest import TestCase, main


class MovieTests(TestCase):
    def test_init_works(self):
        movie = Movie('test', 2000, 5.5)
        self.assertEqual('test', movie.name)
        self.assertEqual(2000, movie.year)
        self.assertEqual(5.5, movie.rating)
        self.assertEqual([], movie.actors)

    def test_name_prop(self):
        movie = Movie('test', 2000, 5.5)
        self.assertEqual('test', movie._Movie__name)

    def test_name_setter_invalid_name_raises(self):
        movie = Movie('test', 2000, 5.5)
        with self.assertRaises(ValueError) as ex:
            movie.name = ''
        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_year_prop(self):
        movie = Movie('test', 2000, 5.5)
        self.assertEqual(2000, movie._Movie__year)

    def test_year_setter_invalid_year_raises(self):
        movie = Movie('test', 2000, 5.5)
        with self.assertRaises(ValueError) as ex:
            movie.year = 1845
        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_add_actor_happy_case(self):
        movie = Movie('test', 2000, 5.5)
        movie.add_actor('name1')
        self.assertTrue('name1' in movie.actors)
        self.assertTrue(len(movie.actors) == 1)

    def test_add_actor_which_is_added(self):
        movie = Movie('test', 2000, 5.5)
        movie.add_actor('name1')
        result = movie.add_actor('name1')
        self.assertTrue('name1' in movie.actors)
        self.assertTrue(len(movie.actors) == 1)
        self.assertEqual("name1 is already added in the list of actors!", result)

    def test_greater_than_rating_self_is_greater(self):
        movie = Movie('test', 2000, 5.5)
        other = Movie('test2', 2000, 5.3)
        self.assertEqual('"test" is better than "test2"', movie > other)

    def test_is_greater_other_is_greater(self):
        movie = Movie('test', 2000, 5.5)
        other = Movie('test2', 2000, 5.6)
        self.assertEqual('"test2" is better than "test"', movie > other)

    def test_repr_method(self):
        movie = Movie('test', 2000, 5.5)
        movie.add_actor('name1')
        movie.add_actor('name2')
        expected = "Name: test\nYear of Release: 2000\nRating: 5.50\nCast: name1, name2"
        self.assertEqual(expected, repr(movie))


if __name__ == '__main__':
    main()


