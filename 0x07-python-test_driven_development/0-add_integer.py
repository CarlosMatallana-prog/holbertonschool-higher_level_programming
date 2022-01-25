#!/usr/bin/python3
""" 0-add_integer """


def add_integer(a, b=98):
    """ add_integer: Adds two numbers a + b """
    if type(a) in (int, float):
        a = int(a)
    else:
        raise TypeError('a must be an integer')
    if type(b) in (int, float):
        b = int(b)
    else:
        raise TypeError('b must be an integer')
    return a + b
