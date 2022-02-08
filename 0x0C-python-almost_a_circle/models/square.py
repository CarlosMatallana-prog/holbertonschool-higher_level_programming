#!/usr/bin/python3
""" squaer.py """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ __init__ method """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ custom __str__ method """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
