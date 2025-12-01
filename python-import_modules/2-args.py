#!/usr/bin/python3
import sys
arguments = sys.argv
if len(arguments) == 1:
    print("{} arguments.".format(0))
elif len(arguments) == 2:
    print("{} argument:\n{}: {}".format(len(arguments)-1, len(arguments)-1, arguments[len(arguments)-1]))
elif len(arguments) > 2:
    print("{} arguments:".format(len(arguments)-1))
    for i in range(len(arguments)):
        print("{}: {}".format(i, arguments[i+1]))
