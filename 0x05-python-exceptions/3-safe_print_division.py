#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        a / b
    except:
        return None
    finally:
        print("Inside result: {}".format(a / b))
