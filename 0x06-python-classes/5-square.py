#!/usr/bin/python3
"""An empty Square class"""


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
        """Returns the area"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Get the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size"""
        if isinstance(value, (int)) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        elif self.__size > 0:
            for rows in range(0, self.__size):
                for columns in range(0, self.__size):
                    print("#", end=' ')
                print()
