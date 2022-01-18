#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [];
    for delta in range(my_list_1):
        try:
            result = my_list_1[delta] / my_list_2[delta]
        except(IndexError):
            print("out of range")
            result = 0
        except (ValueError, TypeError):
            print("wrong type")
            result = 0
        except(ZeroDivisionError):
            print("division by 0")
            result = 0
        finally:
            new_list.insert(delta, result)
    return new_list
