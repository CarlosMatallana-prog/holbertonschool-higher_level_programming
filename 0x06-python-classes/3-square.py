#!/usr/bin/python3


class Square:
    """Defines a class Square"""

    def __init__(self, size=0):
        """Initializes the data."""
        if isinstance(size, (int)) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
