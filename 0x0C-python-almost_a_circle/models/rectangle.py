#!/usr/bin/python3
""" rectangle.py """
from models.base import Base


class Rectangle(Base):
    """ Rectangle Class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init method """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Get the width"""
        return self.__width

    @width.setter
    def width(self, number_input):
        """ Set the width """
        self.validate_number("width", number_input)
        if number_input <= 0:
            raise ValueError("width must be > 0")
        self.__width = number_input

    @property
    def height(self):
        """ Get the height"""
        return self.__height

    @height.setter
    def height(self, number_input):
        """ Set the height """
        self.validate_number("height", number_input)
        if number_input <= 0:
            raise ValueError("height must be > 0")
        self.__height = number_input

    @property
    def x(self):
        """ Get x """
        return self.__x

    @x.setter
    def x(self, number_input):
        """ Set x """
        self.validate_number("x", number_input)
        if number_input <= 0:
            raise ValueError("x must be > 0")
        self.__x = number_input

    @property
    def y(self):
        """ Get y """
        return self.__y

    @y.setter
    def y(self, number_input):
        """ Set y """
        self.validate_number("y", number_input)
        if number_input <= 0:
            raise ValueError("y must be > 0")
        self.__y = number_input

    def validate_number(self, method, number_input):
        """ check if the input is an integer """
        if type(number_input) is not int:
            raise TypeError("{} must be an integer".format(method))
