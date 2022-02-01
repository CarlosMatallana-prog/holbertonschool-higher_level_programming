#!/usr/bin/python3
""" MyList class """


class MyList(list):
    """ prints the list, but sorted (ascending sort) """

    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) """
        print(sorted(self))
