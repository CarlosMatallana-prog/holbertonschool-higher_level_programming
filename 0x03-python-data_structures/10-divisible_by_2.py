#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            boolean = True
        else:
            boolean = False
        new_list.append(boolean)
    return new_list
