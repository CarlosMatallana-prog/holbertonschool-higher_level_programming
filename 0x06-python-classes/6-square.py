#!/usr/bin/python3
"""An empty Square class"""


class Square:
    """Defines a class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data."""
        if isinstance(size, (int)) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size
        self.__position = position

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
        """Prints the square"""
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                br = "\n" * self.__position[1]
                print(br, end='')
            for rows in range(0, self.__size):
                for columns in range(0, self.__size + self.__position[0]):
                    if columns >= self.__position[0]:
                        print("#", end='')
                    else:
                        print(" ", end='')
                print()

    @property
    def position(self):
        """Get the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position"""
        if (type(value) is not tuple or
                len(value) != 2 or
                type(value[0]) is not int or
                type(value[1]) is not int or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
