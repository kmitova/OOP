from project.library import Library
from unittest import TestCase, main


class LibraryTests(TestCase):
    def test_init_is_correct(self):
        library = Library('test')
        self.assertEqual('test', library.name)
        self.assertEqual({}, library.books_by_authors)
        self.assertEqual({}, library.readers)

    def test_name_setter(self):
        library = Library('test')
        library.name = 'test 1'
        self.assertEqual('test 1', library.name)

    def test_name_setter_invalid_raises(self):
        library = Library('test')
        with self.assertRaises(ValueError) as ex:
            library.name = ''
        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_add_book_if_author_and_book_not_in_books_by_authors(self):
        library = Library('test')
        library.add_book('author1', 'book1')
        self.assertTrue(len(library.books_by_authors) == 1)
        self.assertTrue(len(library.books_by_authors['author1']) == 1)
        library.add_book('author1', 'book2')
        self.assertTrue(len(library.books_by_authors) == 1)
        self.assertTrue(len(library.books_by_authors['author1']) == 2)
        library.add_book('author2', 'book2')
        self.assertTrue(len(library.books_by_authors) == 2)
        self.assertTrue(len(library.books_by_authors['author1']) == 2)
        self.assertTrue(len(library.books_by_authors['author2']) == 1)

    def test_add_new_reader(self):
        library = Library('test')
        library.add_reader('name')
        self.assertEqual(1, len(library.readers))
        self.assertTrue(len(library.readers) == 1)

    def test_add_existing_reader(self):
        library = Library('test')
        library.add_reader('name')
        self.assertEqual(1, len(library.readers))
        self.assertTrue(len(library.readers) == 1)
        result = library.add_reader('name')
        self.assertEqual("name is already registered in the test library.", result)

    def test_rent_book_if_reader_not_in_readers(self):
        library = Library('test')
        result = library.rent_book('name', 'author1', 'title1')
        self.assertTrue(len(library.readers) == 0)
        self.assertEqual("name is not registered in the test Library.", result)

    def test_if_author_is_not_in_books_by_authors(self):
        library = Library('test')
        library.add_reader('name')
        result = library.rent_book('name', 'author1', 'title1')
        self.assertTrue(len(library.books_by_authors) == 0)
        self.assertEqual("test Library does not have any author1's books.", result)

    def test_if_book_is_not_available_to_rent(self):
        library = Library('test')
        library.add_reader('name')
        library.add_book('author1', 'title1')
        result = library.rent_book('name', 'author1', 'title2')
        self.assertEqual("""test Library does not have author1's "title2".""", result)

    def test_rent_book_happy_case(self):
        library = Library('test')
        library.add_reader('name')
        library.add_book('author1', 'title1')
        library.rent_book('name', 'author1', 'title1')
        self.assertTrue(len(library.readers['name']) == 1)
        self.assertEqual(0, len(library.books_by_authors['author1']))







if __name__ == '__main__':
    main()