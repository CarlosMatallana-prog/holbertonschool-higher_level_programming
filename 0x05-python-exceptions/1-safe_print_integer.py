#!/usr/bin/python3
def safe_print_integer(value):
    if int(value):
        try:
            print("{:d}".format(value), end='')
            print()
            return True
        except:
            return False
