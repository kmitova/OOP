from project.library import Library
from unittest import TestCase, main


class LibraryTests(TestCase):
    def test_init_works(self):
        lib = Library('test')
        self.assertEqual({}, lib.books_by_authors)
        self.assertEqual({}, lib.readers)
        self.assertEqual('test', lib.name)

    def test_name_setter_invalid_raises(self):
        lib = Library('test')
        with self.assertRaises(ValueError) as ex:
            lib.name = ''
        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_add_book_new_author(self):
        lib = Library('test')
        lib.add_book('author1', 'book1')
        self.assertEqual({'author1': ['book1']}, lib.books_by_authors)

    def test_add_book_old_author(self):
        lib = Library('test')
        lib.add_book('author1', 'book1')
        lib.add_book('author1', 'book2')
        self.assertEqual({'author1': ['book1', 'book2']}, lib.books_by_authors)

    def test_add_existing_author_and_book(self):
        lib = Library('test')
        lib.add_book('author1', 'book1')
        self.assertEqual({'author1': ['book1']}, lib.books_by_authors)
        lib.add_book('author1', 'book1')
        self.assertEqual({'author1': ['book1']}, lib.books_by_authors)

    def test_add_reader_new(self):
        lib = Library('test')
        lib.add_reader('reader1')
        self.assertEqual(1, len(lib.readers))
        self.assertEqual({'reader1': []}, lib.readers)

    def test_add_reader_existing(self):
        lib = Library('test')
        lib.add_reader('reader1')
        self.assertEqual(1, len(lib.readers))
        self.assertEqual({'reader1': []}, lib.readers)
        result = lib.add_reader('reader1')
        self.assertEqual(1, len(lib.readers))
        self.assertEqual({'reader1': []}, lib.readers)
        self.assertEqual("reader1 is already registered in the test library.", result)

    def test_rent_book_not_existing_reader(self):
        lib = Library('test')
        # lib.add_book('author1', 'book1')
        result = lib.rent_book('reader1', 'author1', 'title1')
        self.assertEqual("reader1 is not registered in the test Library.", result)

    def test_rent_book_not_existing_author(self):
        lib = Library('test')
        lib.add_reader('reader1')
        result = lib.rent_book('reader1', 'author1', 'title1')
        self.assertEqual("test Library does not have any author1's books.", result)

    def test_rent_invalid_book(self):
        lib = Library('test')
        lib.add_reader('reader1')
        lib.add_book('author1', 'book1')
        result = lib.rent_book('reader1', 'author1', 'title2')
        self.assertEqual("""test Library does not have author1's "title2".""", result)

    def test_rent_valid(self):
        lib = Library('test')
        lib.add_reader('reader1')
        lib.add_book('author1', 'title1')
        lib.rent_book('reader1', 'author1', 'title1')
        self.assertEqual({'reader1': [{'author1': "title1"}]}, lib.readers)
        self.assertEqual(0, len(lib.books_by_authors['author1']))


if __name__ == "__main__":
    main()
