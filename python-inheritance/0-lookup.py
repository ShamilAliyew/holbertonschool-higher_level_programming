#!/usr/bin/python3
"""the list of available attributes and methods of an object"""


class MyClass:
    """a function that returns the list of available attributes and methods of an object"""
    name = "MyClass"
    count = 1
    def anyFunction(self):
        pass

def lookup(cls):
    return cls.__dict__
