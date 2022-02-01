#!/usr/bin/python3
""" inherits_from Class """


def inherits_from(obj, a_class):
    """ Check if the object is an instance of a class that inherited  """
    if type(obj) is a_class:
        return False
    elif isinstance(obj, a_class):
        return True
    else:
        return False
