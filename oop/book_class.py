#!/usr/bin/python3
"""
Defines a Book class with magic methods.
"""

class Book:
    """
    A class to represent a Book.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        year (int): The publication year of the book.
    """
    def __init__(self, title, author, year):
        """
        Initializes a new Book instance.
        """
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' created.")

    def __del__(self):
        """
        Handles the deletion of a Book instance.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns an informal string representation of the Book.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns an official string representation of the Book.
        """
        return f"Book('{self.title}', '{self.author}', {self.year}')"
