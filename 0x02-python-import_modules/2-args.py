#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if length == 1:
        print("0 arguments.")
    else:
        if length == 2:
            str = "argument"
        else:
            str = "arguments"
        print("{} {}:".format(length - 1, str))
        for i in range(1, length):
            print("{}: {}".format(i, sys.argv[i]))
