#!/usr/bin/python3
""" rectangle.py """
from models.base import Base
from collections import OrderedDict


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
    def width(self, width_input):
        """ Set the width """
        self.check_number("width", width_input)
        if width_input <= 0:
            raise ValueError("width must be > 0")
        self.__width = width_input

    @property
    def height(self):
        """ Get the height"""
        return self.__height

    @height.setter
    def height(self, height_input):
        """ Set the height """
        self.check_number("height", height_input)
        if height_input <= 0:
            raise ValueError("height must be > 0")
        self.__height = height_input

    @property
    def x(self):
        """ Get x """
        return self.__x

    @x.setter
    def x(self, x_input):
        """ Set x """
        self.check_number("x", x_input)
        if x_input < 0:
            raise ValueError("x must be >= 0")
        self.__x = x_input

    @property
    def y(self):
        """ Get y """
        return self.__y

    @y.setter
    def y(self, y_input):
        """ Set y """
        self.check_number("y", y_input)
        if y_input < 0:
            raise ValueError("y must be >= 0")
        self.__y = y_input

    def check_number(self, method, number_input):
        """ check if the input is an integer """
        if type(number_input) is not int:
            raise TypeError("{} must be an integer".format(method))

    def area(self):
        """ returns the triangle area """
        return self.width * self.height

    def display(self):
        """ Prints the rectangle """
        print("\n" * self.y, end='')
        for i in range(self.height):
            for j in range(self.width + self.x):
                if j < self.x:
                    print(' ', end='')
                else:
                    print('#', end='')
            print('')

    def __str__(self):
        """ Custom str method """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """

        if bool(args) is True and args is not None:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            for i in kwargs.keys():
                if i in dir(self):
                    setattr(self, i, kwargs[i])

    def to_dictionary(self):
        """  returns the dictionary representation of a Rectangle """
        ret_dict = OrderedDict()
        ret_dict["id"] = self.id
        ret_dict["width"] = self.width
        ret_dict["height"] = self.height
        ret_dict["x"] = self.x
        ret_dict["y"] = self.y
        return dict(ret_dict)
