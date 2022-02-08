#!/usr/bin/python3
""" base.py """
import json


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

    def to_json_string(list_dictionaries):
        """  returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or bool(list_dictionaries) is False:
            return "[]"
        return json.dumps(list_dictionaries)
