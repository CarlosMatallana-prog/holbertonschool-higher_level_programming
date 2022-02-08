#!/usr/bin/python3
""" base.py """
import json
import csv


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

    def save_to_file(cls, list_objs):
        filename = "{}.json".format(cls.__name__)
        list_dict = []
        if list_objs is None:
            pass
        else:
            list_dict = list(map(cls.to_dictionary, list_objs))

        with open(filename, "w") as json_txt_file:
            json_txt_file.write(cls.to_json_string(list_dict))

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON format string of the object """
        if list_dictionaries is None or bool(list_dictionaries) is False:
            return "[]"
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        filename = "{}.csv".format(cls.__name__)
        if list_objs:
            list_of_dictionaries = list(map(cls.to_dictionary, list_objs))
            list_of_headers = list(list_of_dictionaries[0].keys())
        with open(filename, 'w', newline='') as csv_file:
            if list_objs is None or bool(list_objs) is False:
                csv_file.write("[]")
            else:
                writer = csv.DictWriter(csv_file, list_of_headers)
                writer.writeheader()
                writer.writerows(list_of_dictionaries)
