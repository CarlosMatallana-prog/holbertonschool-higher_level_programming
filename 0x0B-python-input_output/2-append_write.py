#!/usr/bin/python3
""" 2-append_write """


def append_write(filename="", text=""):
    """ append_write class """
    with open(filename, "a", encoding='utf-8') as the_file:
        return(the_file.write(text))
