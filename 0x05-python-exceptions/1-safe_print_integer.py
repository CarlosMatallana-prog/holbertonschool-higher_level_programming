#!/usr/bin/python3
def safe_print_integer(value):
    if type(value) == int:
        try:
            print("{:d}".format(value), end='')
            print()
            return True
        except:
            return False
