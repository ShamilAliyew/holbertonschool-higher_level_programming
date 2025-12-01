#!/usr/bin/python3
import sys
from curses.ascii import isdigit

if __name__ == "__main__":
    arguments = sys.argv[1:]
    sumarg = 0
    for i in range(len(arguments)):
        if arguments[i].isdigit() or (arguments[i].startswith('-')
                                      and arguments[i][1:].isdigit()):
            sumarg += int(arguments[i])
        else:
            continue
    print(sumarg)
