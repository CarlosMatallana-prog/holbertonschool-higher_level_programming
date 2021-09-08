#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastn = number % 10
if number < 0:
    lastn = (((number * -1) % 10)) * -1
if lastn > 5:
    to_print = "greater than 5"
if lastn == 0:
    to_print = "0"
if lastn < 6 and lastn != 0:
    to_print = "less than 6 and not 0"
print("Last digit of {:d} is {:d} and is {:s}".format(number, lastn, to_print))
