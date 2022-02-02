#!/usr/bin/python3
""" 0-read_file """


def read_file(filename=""):
    """ read_file class """
    with open("{}".format(filename), "r", encoding='utf-8') as the_file:
        print(the_file.read(), end='')
