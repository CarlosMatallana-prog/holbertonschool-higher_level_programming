#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    another_list = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return another_list
    another_list[idx] = element
    return another_list
