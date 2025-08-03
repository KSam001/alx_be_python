class Book:
    """
    Represents a book with a title, author, and a checked-out status.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Marks the book as returned."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is not checked out, False otherwise."""
        return not self._is_checked_out

class Library:
    """
    Manages a collection of books.
    """
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a new book to the library's collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """
        Checks out a book from the library by its title.
        Prints a message if the book is not found or is already checked out.
        """
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    print(f"'{title}' has been successfully checked out.")
                    return
                else:
                    print(f"Error: '{title}' is already checked out.")
                    return
        print(f"Error: '{title}' not found in the library.")

    def return_book(self, title):
        """
        Returns a book to the library by its title.
        Prints a message if the book is not found or is not checked out.
        """
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    print(f"'{title}' has been successfully returned.")
                    return
                else:
                    print(f"Error: '{title}' was not checked out.")
                    return
        print(f"Error: '{title}' not found in the library.")

    def list_available_books(self):
        """Prints a list of all available books in the library."""
        print("Available books:")
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
