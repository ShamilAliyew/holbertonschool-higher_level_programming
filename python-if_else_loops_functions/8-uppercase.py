#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if ord(s) >= ord('a') or ord(s) <= ord('z'):
            print(chr(ord(s)-32), end=' ')
        else:
            print(s, end=' ')
