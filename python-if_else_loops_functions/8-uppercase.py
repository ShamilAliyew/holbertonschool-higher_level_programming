#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if ord(s) >= ord('a') and ord(s) <= ord('z'):
            print('{}'.format(chr(ord(s)-32)), end='')
        else:
            print('{}'.format(s), end='')
uppercase("Best School 98 Battery street")