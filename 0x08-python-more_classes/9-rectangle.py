#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Class Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the data."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                    string += str(self.print_symbol)
                    rows += 1
                string += '\n'
                colums += 1
            return string[0: -1]
        else:
            return string

    def __repr__(self):
        """ custom __repr__ method """
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """ custom __del__ method """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the biggest rectangle based on the area """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """ Returns the size square """
        return cls(size, size)
