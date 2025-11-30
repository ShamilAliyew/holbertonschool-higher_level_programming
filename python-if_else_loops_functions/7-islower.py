#!/usr/bin/python3
def islower(s):
    l = []
    for i in range(97, 123):
        l.append(chr(i))
    if s in l:
        return True
    else:
        return False
