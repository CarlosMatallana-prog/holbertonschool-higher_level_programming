#!/usr/bin/python3
def uniq_add(my_list=[]):
    i, j = 0, 0
    remove_doble = list(set(my_list))
    for i in remove_doble:
        j += i
    return j
