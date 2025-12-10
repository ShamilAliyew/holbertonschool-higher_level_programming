#!/usr/bin/python3
"""the list of available attributes and methods of an object"""


def lookup(cls):
    """a function that returns the list of available attributes and
     methods of an object"""
    return cls.__dict__
