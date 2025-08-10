#!/usr/bin/python3
"""
A module demonstrating polymorphism and method overriding.
"""
import math

class Shape:
    """Base class for geometric shapes."""
    def area(self):
        """Calculates the area of the shape."""
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    """A derived class for a rectangle."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Overrides the area method to calculate a rectangle's area."""
        return self.length * self.width

class Circle(Shape):
    """A derived class for a circle."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Overrides the area method to calculate a circle's area."""
        return math.pi * (self.radius ** 2)
