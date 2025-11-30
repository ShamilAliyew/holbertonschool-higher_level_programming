#!/usr/bin/python3
def islower(s):
    if not s:
        raise Exception('Empty string not allowed')
    l = []
    for i in range(93, 127):
        l.append(chr(i))
    if s in l:
        return True
    else:
        return False
print(islower(''))