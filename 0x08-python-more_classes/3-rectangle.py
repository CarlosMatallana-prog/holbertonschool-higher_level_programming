#!/usr/bin/python3
"""Empty class Rectangle"""


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
                self.__height = value  #: Set private __height value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """Get the width"""
        return self.__width

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

    def area(self):
        """ Get the area"""
        return self.height * self.width

    def perimeter(self):
        """ Set the perimeter """
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return 2 * self.height + 2 * self.width

    def __str__(self):
        """ custom __str__ method """
        string = ''
        if self.height > 0 and self.width > 0:
            colums = 0
            while colums < self.height:
                rows = 0
                while rows < self.width:
                    string += '#'
                    rows += 1
                string += '\n'
                colums += 1
            return string[0: -1]
        else:
            return string
