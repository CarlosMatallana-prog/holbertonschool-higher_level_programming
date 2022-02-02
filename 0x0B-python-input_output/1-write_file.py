#!/usr/bin/python3
""" 1-write_file """


def write_file(filename="", text=""):
    """ write_file class """
    with open(filename, "w", encoding='utf-8') as the_file:
        return(the_file.write(text))
