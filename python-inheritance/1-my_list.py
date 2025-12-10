#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """a class MyList that inherits from list"""
    def __init__(self):
        pass
    def print_sorted(self):
        print(sorted(self))