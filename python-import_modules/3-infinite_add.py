#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments = sys.argv[1:]
    sumarg = 0
    for i in range(len(arguments)):
        sumarg += int(arguments[i])
    print(sumarg)