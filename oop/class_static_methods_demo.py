#!/usr/bin/python3
"""
A module demonstrating class and static methods.
"""

class Calculator:
    """A class to perform simple calculations."""
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Returns the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Returns the product of two numbers and prints the class attribute.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
