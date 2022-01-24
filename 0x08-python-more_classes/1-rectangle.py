#!/usr/bin/python3


class Rectangle:
    """Class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the data."""
        self.width = width
        self.height = height

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height"""
        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """Get the width"""
        return self.__width()

    @width.setter
    def width(self, value):
        """Set the width"""
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
