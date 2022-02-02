#!/usr/bin/python3
""" 11-student """


class Student():
    """ Student class """
    first_name = ""
    last_name = ""
    age = ""

    def __init__(self, first_name, last_name, age):
        """ __init__ function """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns the dictionary representation of a Student """

        if type(attrs) is list:
            new_dict = {}
            for key in attrs:
                try:
                    new_dict[key] = self.__dict__[key]
                except KeyError:
                    pass
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """ rebuilds a Student's attrs """
        for key in json.keys():
            self.__dict__[key] = json[key]
