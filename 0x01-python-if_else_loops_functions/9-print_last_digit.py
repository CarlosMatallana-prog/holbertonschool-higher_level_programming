#!/usr/bin/python3
def print_last_digit(number):
    lastn = number % 10
    if number < 0:
        lastn = (((number * -1) % 10))
    print("{:d}".format(lastn), end="")
    return lastn
