#!/usr/bin/python3

"""Define a class Sqaure."""


class Square:
    """Represent a square."""


    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int):the size of the create square.
        """

        if not isinstance(size, int):
            raise TypeErrpr("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >=0")

        self.__size = size

    def area(self):
        """A method that returns the current square area"""
        return (self.__size * self.__size)
