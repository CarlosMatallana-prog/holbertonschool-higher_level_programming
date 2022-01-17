#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    if len(my_list_1) > len(my_list_2):
        eval_list(my_list_1, my_list_2, my_list_1)
    else:
        eval_list(my_list_1, my_list_2, my_list_2)


def eval_list(my_list_1, my_list_2, list_limit):
    new_list = []
    for delta in range(0, len(list_limit)):
        result = None
        try:
            result = my_list_1[delta] / my_list_2[delta]
        except(IndexError):
            print("out of range")
            new_list.insert(delta, 0)
        except (TypeError):
            print("wrong type")
            new_list.insert(delta, 0)
        except(ZeroDivisionError):
            print("division by 0")
            new_list.insert(delta, 0)
        finally:
            new_list.insert(delta, result)
    return new_list
