#!/usr/bin/python3
"""
A library system that uses inheritance and composition.
"""

class Book:
    """Base class for a book."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        """Returns a string representation of the book."""
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """Derived class for an E-Book."""
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Returns a string representation of the E-Book."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """Derived class for a print book."""
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Returns a string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """A class to manage a collection of books."""
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Adds a book to the library's collection."""
        self.books.append(book)

    def list_books(self):
        """Prints the details of each book in the library."""
        for book in self.books:
            print(book)
