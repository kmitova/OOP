from project.movie import Movie
from unittest import TestCase, main


class MovieTests(TestCase):
    def test_init_is_correct(self):
        movie = Movie("lotr", 2000, 5.0)
        self.assertEqual('lotr', movie.name)
        self.assertEqual(2000, movie.year)
        self.assertEqual(5.0, movie.rating)
        self.assertEqual([], movie.actors)

    def test_invalid_name_setter_raises(self):
        movie = Movie("lotr", 2000, 5.0)
        with self.assertRaises(ValueError) as ex:
            movie.name = ''
        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_invalid_year_setter_raises(self):
        movie = Movie("lotr", 2000, 5.0)
        with self.assertRaises(ValueError) as ex:
            movie.year = 1000
        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_add_actor_new(self):
        movie = Movie("lotr", 2000, 5.0)
        movie.add_actor('name1')
        self.assertTrue('name1' in movie.actors)
        self.assertTrue(len(movie.actors) == 1)

    def test_add_existing_actor(self):
        movie = Movie("lotr", 2000, 5.0)
        movie.actors = ['name1']
        result = movie.add_actor('name1')
        self.assertTrue(len(movie.actors) == 1)
        self.assertEqual("name1 is already added in the list of actors!", result)

    def test_greater_than_if_movie_rating_is_greater_than_other_rating(self):
        movie = Movie("lotr", 2000, 5.0)
        other = Movie("other", 2000, 4.9)
        result = movie > other
        self.assertEqual('"lotr" is better than "other"', result)

    def test_greater_than_if_other_rating_is_greater_than_movie_rating(self):
        movie = Movie("lotr", 2000, 4.0)
        other = Movie("other", 2000, 4.9)
        result = movie > other
        self.assertEqual('"other" is better than "lotr"', result)

    def test_repr_method(self):
        movie = Movie("lotr", 2000, 4.0)
        movie.actors = ['name', 'another name']
        expected = "Name: lotr\nYear of Release: 2000\nRating: 4.00\nCast: name, another name"
        result = repr(movie)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
