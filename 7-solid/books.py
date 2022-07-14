class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        # self.location = location
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        try:
            return [book for book in self.books if book.title == title][0]
        except IndexError:
            return 'Book not found'


library = Library()

for num in range(1, 21):
    book = Book(f'Title {num}', f"Author {num}")
    library.add_book(book)





