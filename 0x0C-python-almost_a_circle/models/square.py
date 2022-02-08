#!/usr/bin/python3
""" square.py """
from models.rectangle import Rectangle
from collections import OrderedDict


class Square(Rectangle):
    """ square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ __init__ method """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ custom __str__ method """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """ get the size """
        return self.width

    @size.setter
    def size(self, number):
        """ Set the size """
        self.width = number
        self.height = number

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        if bool(args) is True and args is not None:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except Exception as e:
                pass
        else:
            for i in kwargs.keys():
                if i in dir(self):
                    setattr(self, i, kwargs[i])

    def to_dictionary(self):
        """  returns the dictionary representation of a Rectangle """
        ret_dict = OrderedDict()
        ret_dict["id"] = self.id
        ret_dict["size"] = self.width
        ret_dict["x"] = self.x
        ret_dict["y"] = self.y
        return dict(ret_dict)
