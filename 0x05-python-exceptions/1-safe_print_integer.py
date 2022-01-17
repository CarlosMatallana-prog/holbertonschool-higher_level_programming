#!/usr/bin/python3
def safe_print_integer(value):
    if type(value) == int:
        try:
            print("{:d}".format(value), end='')
            print()
        except:
            return False
        return True
    else:
        return False
