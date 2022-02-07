#!/usr/bin/python3
""" base.py """
import json
import csv
from collections import OrderedDict


class Base():
    """ Class: Base """

    __nb_objects = 0

    def __init__(self, id=None):
        """ __init__: """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
