#!/usr/bin/python3
""" Square class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square class, inherits from Rectangle """

    def __init__(self, size):
        """ init method  """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ return de rectangle area"""
        return super().area()

    def __str__(self):
        """ custom str method """
        return("[Square] {}/{}".format(self.__size, self.__size))
