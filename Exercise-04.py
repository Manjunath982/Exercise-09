class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_number_of_books(self):
        return len(self.books)

    def list_books(self):
        return [str(book) for book in self.books]


def main():
    library = Library()

    # Add some books to the library
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))

    # Get and print the number of books
    print("Number of books in the library:", library.get_number_of_books())

    # List and print all books
    print("Books in the library:")
    for book in library.list_books():
        print(book)


if __name__ == "__main__":
    main()
