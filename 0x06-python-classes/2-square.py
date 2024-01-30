#!/usr/bin/python3

"""Define a square class."""


class Square:
    """A square"""
    

    def __init__(self, size=0):
        """Initialiazation of new square.

        Args:
            size (int): The square's size.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
