#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and the list of arguments."""
    import sys

    arg_no = len(sys.argv) - 1
    if arg_no == 0:
        print("0 arguments.")
    elif arg_no == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_no))

    for i in range(arg_no):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
