#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    nargs = len(argv)
    if nargs == 1:
        print("0")
    elif nargs == 2:
        print("{}".format(argv[1]))
    elif nargs > 2:
        result = 0
        for argument in argv[1:]:
            result = result + int(argument)
        print(result)
