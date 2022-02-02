#!/usr/bin/python3
""" 8-class_to_json """


def class_to_json(obj):
    """ class_to_json function """
    return dict(obj.__dict__)
