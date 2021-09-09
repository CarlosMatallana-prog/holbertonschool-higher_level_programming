#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = len(sys.argv)

    if args == 2:
        print("1 argument:".format(args - 1))
        print("1: {:s}".format(sys.argv[1]))
    elif args > 2:
        print("{:d} arguments:".format(args - 1))
        counter = 1
        while counter < args:
            print("{:d}: {:s}".format(counter, sys.argv[counter]))
            counter += 1
    else:
        print("0 arguments.")
