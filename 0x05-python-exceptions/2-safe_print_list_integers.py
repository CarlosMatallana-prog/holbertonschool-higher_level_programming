#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    c = 0
    while (i < x):
        try:
            if type(my_list[i]) == int:
                print("{}".format(my_list[i]), end='')
                c = c + 1
            i = i + 1
        except (ValueError, TypeError):
            pass

    print()
    return c
